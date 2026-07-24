#!/usr/bin/env bash

set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv_dir="${project_dir}/.venv"
python_bin="${PYTHON:-python3}"

if [[ ! -x "${venv_dir}/bin/python" ]]; then
    "${python_bin}" -m venv "${venv_dir}"
    "${venv_dir}/bin/python" -m pip install --upgrade pip
fi

venv_python="${venv_dir}/bin/python"
venv_bin="${venv_dir}/bin"

"${venv_python}" -m pip install pipenv
PIPENV_IGNORE_VIRTUALENVS=1 \
    PIPENV_VENV_IN_PROJECT=1 \
    "${venv_bin}/pipenv" sync --dev
"${venv_python}" -m pip install --no-build-isolation --no-deps -e "${project_dir}"

source_dir="${project_dir}/patterns"
tests_dir="${project_dir}/tests"

"${venv_bin}/codespell" --quiet-level=2 "${source_dir}" "${tests_dir}" "${project_dir}/README.md"
"${venv_bin}/flake8" \
    "${source_dir}" \
    "${tests_dir}" \
    --max-line-length=120 \
    --extend-ignore=E266,E731,W503 \
    --count \
    --show-source \
    --statistics
"${venv_bin}/isort" --profile black --check-only "${source_dir}" "${tests_dir}"
"${venv_bin}/black" --check "${source_dir}" "${tests_dir}"
"${venv_bin}/mypy" "${source_dir}"
"${venv_bin}/pytest" "${tests_dir}" "${source_dir}"

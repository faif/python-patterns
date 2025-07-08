#! /bin/bash

pip install --upgrade pip
pip install black codespell flake8 isort mypy pytest pyupgrade tox
pip install -e .

source_dir="./patterns"

codespell --quiet-level=2 ./patterns  # --ignore-words-list="" --skip=""
flake8 "${source_dir}"  --count --show-source --statistics
isort --profile black "${source_dir}"
tox 
mypy --ignore-missing-imports "${source_dir}" || true
pytest "${source_dir}"
pytest --doctest-modules "${source_dir}" || true
shopt -s globstar && pyupgrade --py312-plus ${source_dir}/*.py

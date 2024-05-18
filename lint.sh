#! /bin/bash

pip install --upgrade pip
pip install black codespell flake8 isort mypy pytest pyupgrade tox
black --check .
codespell --quiet-level=2  # --ignore-words-list="" --skip=""
flake8 . --count --show-source --statistics
isort --profile black .
tox
pip install -e .
mypy --ignore-missing-imports . || true
pytest .
pytest --doctest-modules . || true
shopt -s globstar && pyupgrade --py37-plus **/*.py
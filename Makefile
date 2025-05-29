.PHONY: venv install lint test run docs

venv:
python3 -m venv .venv
. .venv/bin/activate && pip install -U pip

install: venv
. .venv/bin/activate && pip install -e .[dev]

lint:
. .venv/bin/activate && ruff check ankipp

test:
. .venv/bin/activate && pytest

run:
. .venv/bin/activate && python -m ankipp

docs:
@echo "(placeholder) Génération de la doc Sphinx"

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


export:
	. .venv/bin/activate && ankipp export $(deck) --format $(fmt) --out $(out)
import:
	. .venv/bin/activate && ankipp import $(file)

docs:
@echo "(placeholder) Génération de la doc Sphinx"

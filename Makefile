.PHONY: help
.PHONY: default
default: install


install:
	uv sync --all-extras --all-groups --frozen
	uvx pre-commit install

install-docs:
	uv sync --group docs --frozen --no-group dev

update:
	uv lock
	uvx pre-commit autoupdate
	$(MAKE) install

test: install
	uv run pytest

check: install
	uvx  pre-commit run --all-files

coverage: install
	uv run pytest --cov=protocol_task --cov-report=xml

cov: install
	uv run pytest --cov=protocol_task  --cov-report=term-missing

mypy: install
	uv run mypy protocol_task --config-file pyproject.toml


doctest: install-docs doc

doc:
	uv run --no-sync sphinx-build -M doctest docs/source docs/build/ -W --keep-going --fresh-env
	uv run --no-sync sphinx-build -M html docs/source docs/build/ -W --keep-going --fresh-env

check-all: check test mypy doc

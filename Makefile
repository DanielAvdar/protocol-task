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
	uv run pytest --cov=my_pkg --cov-report=xml # todo: change my_pkg to the actual package name

cov: install
	uv run pytest --cov=my_pkg --cov-report=term-missing # todo: change my_pkg to the actual package name

mypy: install
	uv run mypy my_pkg --config-file pyproject.toml
# todo: chanege my_pkg to the actual package name

doctest: install-docs doc

doc:
	uv run --no-sync sphinx-build -M doctest docs/source docs/build/ -W --keep-going --fresh-env
	uv run --no-sync sphinx-build -M html docs/source docs/build/ -W --keep-going --fresh-env

check-all: check test mypy doc

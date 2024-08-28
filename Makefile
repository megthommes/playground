# Based on:
# https://github.com/fpgmaas/cookiecutter-poetry/blob/main/Makefile
# Florian Maas

.PHONY: install
install: ## Install the poetry environment
	@echo "Creating virtual environment"
	@poetry install
	@if [ ! -d ".git/hooks" ]; then pre-commit install; fi

.PHONY: install-dev
install-dev: ## Install the poetry environment with development dependencies
	@echo "Creating virtual environment with development dependencies"
	@poetry install
	@if [ ! -d ".git/hooks" ]; then pre-commit install; fi

.PHONY: test
test: ## Run tests
	@echo "Running tests"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: test-randomly
test-randomly: ## Run tests in a random order
	@echo "Running tests"
	@poetry run pytest --randomly --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: format
format: ## Format code
	@echo "Formatting code"
	@poetry run isort .
	@poetry run add-trailing-comma .
	@poetry run pyupgrade --py36-plus .
	@poetry run autopep8 .
	@poetry run black .

.PHONY: lint
lint: ## Lint code
	@echo "Linting code"
	@poetry run flake8 .

.PHONY: type-check
type-check: ## Type-check code
	@echo "Type-checking code"
	@poetry run mypy .

.PHONY: validate
validate: format lint type-check ## Run format, lint, and type-check

.PHONY: check
check: validate test ## Run validate and test

.PHONY: pre-commit
pre-commit: ## Run pre-commit checks
	@echo "Running pre-commit checks"
	@poetry run pre-commit run

.PHONY: clean
clean: ## Clean up build artifacts and caches
	@echo "Cleaning up build artifacts and caches"
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -delete
	@rm -rf build dist .egg-info *.egg-info .pytest_cache .mypy_cache .mypy .coverage coverage.xml
	@rm -rf notebooks/.ipynb_checkpoints node_modules

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

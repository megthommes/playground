# Based on:
# https://github.com/fpgmaas/cookiecutter-poetry/blob/main/Makefile
# Florian Maas

.PHONY: install
install: ## Install the poetry environment
	@echo "Creating virtual environment"
	@poetry install
	@if [ ! -d ".git/hooks" ]; then poetry run pre-commit install; fi

.PHONY: install-dev
install-dev: ## Install the poetry environment with development and test dependencies
	@echo "Creating virtual environment with development and test dependencies"
	@poetry install --with test, dev
	@if [ ! -d ".git/hooks" ]; then poetry run pre-commit install; fi

.PHONY: test
test: ## Run tests
	@echo "Running tests"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: test-randomly
test-randomly: ## Run tests in a random order
	@echo "Running tests in random order"
	@poetry run pytest --randomly-seed=random --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: format
format: ## Format code
	@echo "Formatting code"
	@poetry run isort .
	@poetry run add-trailing-comma .
	@poetry run pyupgrade --py38-plus .
	@poetry run black .

.PHONY: lint
lint: ## Lint code
	@echo "Linting code"
	@poetry run flake8 .
	@poetry run bandit -r . -f custom

.PHONY: type-check
type-check: ## Type-check code
	@echo "Type-checking code"
	@poetry run mypy .

.PHONY: validate
validate: format lint type-check ## Run format, lint, and type-check

.PHONY: check
check: validate test ## Run validate and test

.PHONY: pre-commit-staged
pre-commit-staged: ## Run pre-commit checks on staged files
	@echo "Running pre-commit checks on staged files"
	@poetry run pre-commit run --files $(git diff --cached --name-only)

.PHONY: pre-commit-all
pre-commit-all: ## Run pre-commit checks on all files
	@echo "Running pre-commit checks on all files"
	@poetry run pre-commit run --all-files

.PHONY: pre-commit-update
pre-commit-update: ## Update pre-commit hooks
	@echo "Updating pre-commit hooks"
	@poetry run pre-commit autoupdate

.PHONY: clean
clean: ## Clean up build artifacts and caches
	@echo "Cleaning up build artifacts and caches"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@rm -rf build dist .egg-info *.egg-info .pytest_cache .mypy_cache .coverage coverage.xml
	@rm -rf notebooks/.ipynb_checkpoints node_modules

.PHONY: update
update: ## Update poetry dependencies
	@echo "Updating poetry dependencies"
	@poetry update

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%s%s%s\n", $$1, FS, $$2}' | sort -t: -k1,1 -k2 | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

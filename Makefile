SRC:=tools

.PHONY: all
all: help

.PHONY: vet  ## Run linter
vet:
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --exclude=__init__.py $(SRC)
	poetry run black $(SRC)
	poetry run isort $(SRC)
	poetry run mypy $(SRC)
	poetry run vulture --min-confidence=70 $(SRC)

.PHONY: nb  ## Run JupyterLab
nb:
	poetry run jupyter lab --allow-root --no-browser

.PHONY: s   ## Run MLflow-server
s:
	poetry run mlflow server --default-artifact-root $(MLFLOW_STORAGE_PATH) --host 0.0.0.0

.PHONY: help ## View help
help:
	@grep -E '^.PHONY: [a-zA-Z_-]+.*?## .*$$' $(MAKEFILE_LIST) | sed 's/^.PHONY: //g' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

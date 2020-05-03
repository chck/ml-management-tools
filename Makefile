SRC:=tools

.PHONY: all
all: help

.PHONY: vet  ## Run linter
vet:
	poetry run pylint $(SRC)
	poetry run black $(SRC)
	poetry run mypy $(SRC)

.PHONY: help ## View help
help:
	@grep -E '^.PHONY: [a-zA-Z_-]+.*?## .*$$' $(MAKEFILE_LIST) | sed 's/^.PHONY: //g' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

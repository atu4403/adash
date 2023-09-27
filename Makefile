# Makefile for automating release tasks

# Get project name from pyproject.toml
PROJECT_NAME=$(shell grep name pyproject.toml | head -n 1 | awk -F= '{print $$2}' | xargs)

# Get the current version using `rye version`
NEW_VERSION=$(shell rye version)

# Bump type (major, minor, patch). Default is 'patch'.
BUMP_TYPE=patch

# Display help message
help:
	@echo "Available tasks:"
	@echo "  make create-branch    - Create and checkout pre-release branch."
	@echo "  make bump-version     - Update version number. Specify type with BUMP_TYPE (default is 'patch')."
	@echo "  make build-publish    - Build and publish the project."
	@echo "  make gen-docs         - Generate documentation."
	@echo "  make gen-changelog    - Generate CHANGELOG."
	@echo "  make commit           - Commit changes."
	@echo "  make merge-main       - Merge to main branch."
	@echo "  make tag-version      - Tag version."
	@echo "  make delete-branch    - Delete pre-release branch."
	@echo "  make release          - Full release pipeline. Specify bump type with BUMP_TYPE (default is 'patch')."

# Create and checkout pre-release branch
create-branch:
	git checkout -b pre-release

# Update version number
bump-version:
	rye version --bump $(BUMP_TYPE)
	$(eval NEW_VERSION := $(shell rye version))

# Build and publish the project
build-publish:
	rye build -c && rye publish

# Generate documentation
gen-docs:
	pdoc --html --output-dir=docs --force $(PROJECT_NAME)

# Generate CHANGELOG
gen-changelog:
	git cliff --tag $(NEW_VERSION) -o CHANGELOG.md

# Commit changes
commit:
	git add --all
	git commit -m "🚀 new release setup $(NEW_VERSION)"

# Merge to main branch
merge-main:
	git checkout main
	git merge pre-release

# Tag version
tag-version:
	git tag $(NEW_VERSION)

# Delete pre-release branch
delete-branch:
	git branch -D pre-release

# Full release pipeline
release: create-branch bump-version build-publish gen-docs gen-changelog commit merge-main tag-version delete-branch

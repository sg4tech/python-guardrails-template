.PHONY: test-template

# Generate a project from the template and run its `make verify`; PROJECT_NAME,
# PYTHON_VERSION and STRICT_CLI choose the answers.
test-template:
	./scripts/check-template.sh

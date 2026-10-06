.PHONY: test-template

# Generate a project from the template and run its `make verify`; PROJECT_NAME and
# PYTHON_VERSION choose the answers.
test-template:
	./scripts/check-template.sh

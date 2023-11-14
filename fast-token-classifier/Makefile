.PHONY: help setup_venv run_api run_test run_integration_test run_lint run_style run_test run_checks
.PHONY: build_package publish_package

help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment (REQUIRED)."
	@echo "\trun_api:          runs the app."
	@echo "\trun_test:         runs the tests."
	@echo "\trun_lint:         runs the linting."
	@echo "\trun_style:        runs style and type formatting."
	@echo "\trun_checks:       runs tests and code quality (RECOMMENDEED)."
	@echo "\tbuild_package:    used to build the package."
	@echo "\tpublish_package:  used to publish the built the package."
	@echo

setup_venv:
	@echo
	@echo ">>>> Setting up virtual environment. <<<<"
	python3 -m venv venv && . venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -e ".[dev]"

run_api:
	. venv/bin/activate && python3 fast_token_classifier/api/app.py

run_integration_test:
	. venv/bin/activate && pytest -svv -m integration

run_test:
	. venv/bin/activate && pytest -svv

run_lint:
	. venv/bin/activate && ruff fast_token_classifier --fix \
	&& ruff api --fix

run_style:
	. venv/bin/activate && mypy fast_token_classifier \
	&& mypy api

build_package:
	. venv/bin/activate && python3 setup.py clean --all \
	&& python3 setup.py sdist bdist_wheel

run_checks: setup_venv run_test run_lint run_style
	@echo
	@echo ">>>> Running tests and linting. <<<<"

publish_package: run_checks build_package
	@echo
	@echo ">>>> Pushing the package to PyPi. <<<<"
	. venv/bin/activate && twine check dist/* \
	&& twine upload dist/* --verbose

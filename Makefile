.PHONY: help setup_venv run_api run_test run_integration_test run_lint run_style run_test run_checks

help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment."
	@echo "\trun_api:          runs the app."
	@echo "\trun_test:         runs the tests."
	@echo "\trun_lint:         runs the linting."
	@echo "\trun_style:        runs style and type formatting."
	@echo "\trun_checks:       runs tests and code quality (RECOMMENDEED)."
	@echo

setup_venv:
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
	. venv/bin/activate && ruff fast_token_classifier --fix

run_style:
	. venv/bin/activate && mypy fast_token_classifier


run_checks: run_test run_lint run_style

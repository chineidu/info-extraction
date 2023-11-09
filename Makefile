.PHONY: help setup_venv delete_directories run_app run_lint run_style run_test run_checks

help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment."
	@echo "\trun_app:          runs the app."
	@echo "\trun_lint:         runs the linting."
	@echo "\trun_style:        runs style and type formatting."
	@echo "\trun_checks:       runs tests and code quality (RECOMMENDEED)."
	@echo

setup_venv:
	python3 -m venv venv && . venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -e ".[dev]" && python3 src/info_extraction/utils/utilities.py

delete_directories:
	. venv/bin/activate && python3 src/info_extraction/utils/utilities.py

run_app:
	. venv/bin/activate && python3 app/main.py

run_test:
	. venv/bin/activate && pytest -svv

run_lint:
	. venv/bin/activate && ruff src --fix

run_style:
	. venv/bin/activate && mypy src


run_checks: run_test run_lint run_style

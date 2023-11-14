.PHONY: help setup_venv run_api run_test run_lint run_style run_test run_checks


help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment (REQUIRED)."
	@echo "\trun_api:          runs the app."
	@echo "\trun_test:         runs the tests."
	@echo "\trun_lint:         runs the linting."
	@echo "\trun_style:        runs style and type formatting."
	@echo "\trun_checks:       runs tests and code quality (RECOMMENDEED)."
	@echo

setup_venv:
	@echo
	@echo ">>>> Setting up virtual environment. <<<<"
	poetry lock "--no-update" && poetry install --no-interaction

run_test: setup_venv
	poetry run ${MAKE} __test__

__test__:
	pytest -svv -W ignore

run_api:
	poetry run ${MAKE} __run_api__

__run_api__:
	python3 api/app.py

run_lint_n_style:
	poetry run ${MAKE} __run_lint_n_style__

__run_lint_n_style__:
	ruff api --fix && mypy api


run_checks: run_test run_lint_style
	@echo
	@echo ">>>> Running tests and linting. <<<<"

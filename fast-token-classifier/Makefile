.PHONY: help setup_venv run_test run_lint_n_style run_checks publish_package


help:
	@echo "Commands:"
	@echo "\tsetup_venv:          creates a virtual environment (REQUIRED)."
	@echo "\trun_test:            runs the tests."
	@echo "\trun_api:             runs the app."
	@echo "\trun_lint_n_style:    runs linting, style and type formatting."
	@echo "\trun_checks:          runs tests and code quality (RECOMMENDEED)."
	@echo "\tpublish_package:     used to build and publish the package."
	@echo

setup_venv:
	@echo
	@echo ">>>> Setting up virtual environment. <<<<"
	poetry lock "--no-update" && poetry install --no-interaction

run_test: setup_venv
	poetry run ${MAKE} __test__

__test__:
	@echo
	@echo ">>>> Running tests. <<<<"
	pytest -svvW ignore

run_api:
	poetry run ${MAKE} __run_api__

__run_api__:
	@echo
	@echo ">>>> Starting the API. <<<<"
	uvicorn api.app:app --port 8000 --host "0.0.0.0"

run_lint_n_style:
	poetry run ${MAKE} __run_lint_n_style__

__run_lint_n_style__:
	@echo
	@echo ">>>> Running linting. <<<<"
	ruff fast_token_classifier --fix && mypy fast_token_classifier \
	&& ruff api --fix && mypy api

run_checks: run_test run_lint_n_style


publish_package: run_checks
	@echo
	@echo ">>>> Pushing the package to PyPi. <<<<"
	poetry config pypi-token.pypi ${PYPI_TOKEN} \
	&& poetry publish --build --no-interaction
	@echo
	@echo ">>>> DONE! <<<<"

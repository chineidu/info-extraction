# INFO-EXTRACTION

NLP project to identify and categorize named entities in an input text.

## Table of Content

- [INFO-EXTRACTION](#info-extraction)
  - [Table of Content](#table-of-content)
  - [Setup Package](#setup-package)
    - [IMPORTANT STEP](#important-step)
    - [List Available Commands](#list-available-commands)
  - [Build And Publish The Package](#build-and-publish-the-package)
    - [Using Setuptools](#using-setuptools)
    - [Using Poetry](#using-poetry)
  - [Check HugingFace Cache](#check-hugingface-cache)
  - [Run Tests](#run-tests)

## Setup Package

### IMPORTANT STEP

- To setup the package locally, run:

```sh
make setup_venv
```

### List Available Commands

- To list all the available commands, run:

```sh
make help
```

## Build And Publish The Package

### Using Setuptools

- Build the package by running:

```sh
# Install packages required for building and publishing
python -m pip install build twine

# Build
python setup.py clean --all
python setup.py sdist bdist_wheel

# Verify build
twine check dist/*

# Upload package
twine upload dist/* --verbose
```

### Using Poetry

- Build the package using Poetry by running:

```sh
# Install packages required for building and publishing
pip install --no-cache poetry==1.4.2
poetry lock "--no-update" && poetry install --no-interaction

export PYPI_TOKEN="your_pypi_token"
poetry config pypi-token.pypi ${PYPI_TOKEN}

# Build and upload package
poetry publish --build
```

## Check HugingFace Cache

- Check the locally cached models and dataset by running:

```sh
huggingface-cli scan-cache -v
```

## Run Tests

- For unit tests, run:

```sh
# All tests
make run_test
```

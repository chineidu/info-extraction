# INFO-EXTRACTION

NLP project to identify and categorize named entities in an input text.

## Table of Content

- [INFO-EXTRACTION](#info-extraction)
  - [Table of Content](#table-of-content)
  - [Setup Package](#setup-package)
    - [IMPORTANT STEP](#important-step)
  - [Build And Publish The Package](#build-and-publish-the-package)
  - [Check HugingFace Cache](#check-hugingface-cache)
  - [Run Tests](#run-tests)
  - [Start API](#start-api)

## Setup Package

### IMPORTANT STEP

- To setup the package locally, run:

```sh
make setup_venv
```

## Build And Publish The Package

- Build the package by running:

```sh
# Install packages required for building and publishing
python -m pip install build twine

# Build
python setup.py sdist bdist_wheel

# Verify build
twine check dist/*

# Upload package
twine upload dist/* --verbose
```

## Check HugingFace Cache

- Check the locally cached models and dataset by running:

```sh
huggingface-cli scan-cache -v
```

## Run Tests

- For unit and integration tests, run:

```sh
# Integration test
make run_integration_test

# All tests
make run_test
```

## Start API

- To start the API, run:

```sh
make run_api
```

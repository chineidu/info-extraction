# INFO-EXTRACTION

NLP project to identify and categorize named entities in an input text.

## Table of Content

- [INFO-EXTRACTION](#info-extraction)
  - [Table of Content](#table-of-content)
  - [Build The Package](#build-the-package)
  - [Check HugingFace Cache](#check-hugingface-cache)

## Build The Package

- Build the package by running:

```sh
python setup.py sdist bdist_wheel
```

## Check HugingFace Cache

- Check the cached models and dataset by running:

```sh
huggingface-cli scan-cache -v
```

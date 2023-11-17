# API SERVICE

This is the API for making predictions

## Table of Content

- [API SERVICE](#api-service)
  - [Table of Content](#table-of-content)
  - [Setup](#setup)
  - [Docker Setup](#docker-setup)
    - [Image Build](#image-build)
    - [Create Container](#create-container)

## Setup

- To create and install dependencies, run:

```sh
pip install -r requirements.txt
```

## Docker Setup

### Image Build

- Build the docker image by running:

```sh
docker build -t api_service:v2 -f Dockerfile .
```

- **Note**: The model has already been downloaded locally from the [HuggingFace hub](https://huggingface.co/chineidu/bert-finetuned-ner).

### Create Container

- It's assumed that you've downloaded the model.
- Create and run the docker containiner by running:

```sh
export MODEL_DIR="${PWD}/saved_model"

# Without bind mount
docker run -it -p 8000:8005 --rm --name pred_app api_service:v2

# With bind mount
docker run -it -p 8000:8005 --rm \
  -v ${MODEL_DIR}:/opt/saved_model:ro --name pred_app api_service:v2
```

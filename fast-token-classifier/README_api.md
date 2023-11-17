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
export MODEL_DIR="${PWD}/saved_model"
export IMAGE_NAME="api_service"
export TAG="v1"
export APP_NAME="pred_app"

docker build -t ${IMAGE_NAME}:${TAG} -f Dockerfile .
```

- **Note**: The model has already been downloaded locally from the [HuggingFace hub](https://huggingface.co/chineidu/bert-finetuned-ner).

### Create Container

- It's assumed that you've downloaded the model.
- Create and run the docker containiner by running:

```sh
# Without bind mount
docker run -it -p 8000:8005 --rm --name ${APP_NAME} ${IMAGE_NAME}:${TAG}

# With bind mount
docker run -it -p 8000:8005 --rm \
  -v ${MODEL_DIR}:/opt/saved_model:ro --name ${APP_NAME} ${IMAGE_NAME}:${TAG}
```

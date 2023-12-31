# Token Classifier UI

## Table of Content

- [Token Classifier UI](#token-classifier-ui)
  - [Table of Content](#table-of-content)
  - [Setup](#setup)
  - [Docker Setup](#docker-setup)
    - [Image Build](#image-build)
    - [Create Container](#create-container)

## Setup

- To create and install dependencies locally, run:

```sh
poetry lock "--no-update" && poetry install --no-interaction
```

## Docker Setup

### Image Build

- Build the docker image by running:

```sh
export IMAGE_NAME="app_ui_service"
export TAG="v1"
export APP_NAME="simple_app"
export PORT="3008"
export URL=http://pred_app:8005/api/v1/predict

docker build -t ${IMAGE_NAME}:${TAG} -f Dockerfile .
```

### Create Container

- It's assumed that you've downloaded the model.
- Create and run the docker containiner by running:

```sh
docker run -it -p ${PORT}:${PORT} -e URL=${URL} --rm --name ${APP_NAME} ${IMAGE_NAME}:${TAG}
```

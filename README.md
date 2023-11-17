# INFO-EXTRACTION

NLP project to identify and categorize named entities in an input text.

## Table of Content

- [INFO-EXTRACTION](#info-extraction)
  - [Table of Content](#table-of-content)
  - [Build The Image](#build-the-image)
  - [Deploy Locally With Docker](#deploy-locally-with-docker)
    - [Docker Run](#docker-run)
    - [Docker Compose](#docker-compose)

## Build The Image

- Navigate to the `fast-token-classifier` directory.

```sh
export MODEL_DIR="${PWD}/saved_model"
export IMAGE_NAME="your_image_name"
export TAG="your_tag"
export APP_NAME="your_app_name"

cd fast-token-classifier

docker build -t ${IMAGE_NAME}:${TAG}> -f .Dockerfile .
```

## Deploy Locally With Docker

- It's assumed that you're already in the `fast-token-classifier` directory.

### Docker Run

```sh
# With bind mount (required)
docker run -it -p 8000:8005 --rm \
  -v ${MODEL_DIR}:/opt/saved_model:ro --name ${APP_NAME} ${IMAGE_NAME}:${TAG}
```

### Docker Compose

- For more info, check the official [docs](https://docs.docker.com/compose/gettingstarted/)

```sh
# Build and start
docker-compose up --build

# To start
docker-compose up

# To stop
docker-compose down
```

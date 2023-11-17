# INFO-EXTRACTION

NLP project to identify and categorize named entities in an input text.

## Table of Content

- [INFO-EXTRACTION](#info-extraction)
  - [Table of Content](#table-of-content)
  - [Build The Image](#build-the-image)
  - [Deploy Locally With Docker](#deploy-locally-with-docker)
    - [Docker Run](#docker-run)
    - [Docker Compose](#docker-compose)
    - [Kubernetes](#kubernetes)

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

### Kubernetes

- Check my [tutorial](https://github.com/chineidu/MLOps_Tutorials/blob/main/k8s_notes/README.md#delete-resources-in-a-config-file) on how to setup and use K8s.
- You need to push the docker image to a Docker repository e.g. Docker Hub before K8s can access it.

```sh
# Tag the image
docker tag <image_name>:<tag> <new_image_name>:<tag>
# e.g
docker tag my_image:v1.1 chineidu/my_image:v1.1

# Log in
docker login

# Push the (tagged) image
docker push chineidu/my_image:v1.1

# Create a cluster locally
minikube start

# Destoy a cluster locally
minikube stop

# Create deployment
kubectl apply -f <path/to/file(s)>
# e.g
kubectl apply -f k8s/deployment.yaml

# Check the status
# ----------------
# Check the available pods/deployments
kubectl get pods|deployments -n <namespace>
# e.g.
kubectl get pods -n default
kubectl get deployments -n default

# Check the available services
kubectl get services -n <namespace>

# Expose the service
minikube service <service_name> -n <namespace>
# e.g.
minikube service api-service -n default
```

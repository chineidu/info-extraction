# Base image
FROM python:3.10.8

# Create working directory
WORKDIR /opt/src

# Install Poetry
RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache -U pip
RUN pip install --no-cache poetry==1.4.2

# Configuring poetry.
RUN poetry config virtualenvs.create false

# Copy and install dependencies. This should be here to avoid
# re-installing the packages when there's a minor change in the Docker image.
COPY ["./app-api/pyproject.toml", "./opt/src"]
COPY ["./app-api/poetry.lock", "./opt/src"]
RUN poetry install --no-interaction --without dev --no-root

# Copy source code
COPY ["./app-api", "./"]

# Give access to run the run.sh script.
RUN chmod +x run.sh

# Entry point
CMD ["python3", "api/app.py", "--host", "0.0.0.0"]
# CMD ["bash", "./run.sh"]

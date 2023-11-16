FROM python:3.10.8-bullseye

WORKDIR /opt

RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache -U pip
RUN pip install poetry==1.4.2

# First copy & install requirements to speed up the build process in case only the code changes.
COPY ["./pyproject.toml", "./poetry.lock", "./"]

# Disable virtual environment creation
RUN poetry install --no-interaction --no-root -vvv

# Copy the rest of the files.
ADD ["./", "./"]


# CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8005"]
CMD ["poetry", "run", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8005"]

FROM python:3.10.8-bullseye

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache -U pip
RUN pip install poetry==1.7.0

# First copy & install requirements to speed up the build process in case only the code changes.
COPY ["./pyproject.toml", "./poetry.lock", "./"]
RUN touch README.md

# Disable virtual environment creation
RUN poetry install --no-interaction --no-dev --no-root -vvv

# Copy the rest of the files.
ADD ["./", "./"]

RUN poetry install

CMD ["poetry", "run", "python", "frontend/app.py"]

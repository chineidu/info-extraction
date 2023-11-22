FROM python:3.10.8-bullseye

WORKDIR /opt

RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache -U pip
RUN pip install poetry==1.4.2

# First copy & install requirements to speed up the build process in case only the code changes.
COPY ["./pyproject.toml", "./poetry.lock", "README.md", "./"]

# Disable virtual environment creation
RUN poetry install --no-interaction --no-root -vvv

# Copy the rest of the files.
ADD ["./", "./"]

CMD ["poetry", "run", "uvicorn", "src/app.py", "--host", "0.0.0.0", "--port", "8005"]

# Stage 1: Build dependencies
FROM python:3.10-slim-buster AS builder

WORKDIR /opt

COPY ["./requirements.txt", "./"]
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Create final image
FROM python:3.10-slim-buster

WORKDIR /opt

# Copy only the necessary files from the previous stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /opt .

# Copy source code
COPY ["./", "./"]

# Entry point
CMD ["python3", "app.py", "--host", "0.0.0.0"]

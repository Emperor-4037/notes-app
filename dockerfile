# Using slim Python for base image
FROM python:3.11-slim

# Prevent python from writing .pyc files and enable stdout logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Working directory in the container
WORKDIR /app

# Install system dependencies (needed for psycopg2 / builds)
RUN apt-get update && apt-get install -y \
gcc \
libpq-dev \
curl \
&& rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy only dependecy files first (better caching)
COPY pyproject.toml uv.lock ./

# Set uv configuration
ENV UV_HTTP_TIMEOUT=120

# Install dependencies
RUN uv sync

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run app
CMD ["uv", "run", "main.py"]
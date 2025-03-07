# Use an official lightweight Python image.
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    libssl-dev \
    libffi-dev \
    build-essential

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Make port available to the world outside this container
EXPOSE 5001

# Add a delay before running the app
CMD sleep 10 && python app.py

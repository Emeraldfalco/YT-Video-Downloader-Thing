# Use Python image
FROM python:3.10-slim

# Install necessary tools and libraries
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy files (if any local files are required)
# COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir Flask Flask-Cors yt-dlp

# Expose the port
EXPOSE 5000

# Entry point to run the application
CMD ["/bin/bash"]

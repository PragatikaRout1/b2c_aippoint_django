# # Use an official Python runtime as a parent image
# FROM python:3.11-slim
 
# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
 
# # Set the working directory in the container
# WORKDIR /app
 
# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libc6-dev \
#     && rm -rf /var/lib/apt/lists/*
 
# # Install Python dependencies
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir daphne celery

# # Copy the current directory contents into the container at /app
# COPY . /app
 
# # Define environment variables (if needed)
# ENV MEDIA_ROOT /home/ubuntu/media
# ENV LOG_DIR /app/logs
 
# # Create directories for media files and logs
# RUN mkdir -p ${MEDIA_ROOT}
# RUN mkdir -p ${LOG_DIR}
 
# # Create an empty log file
# RUN touch ${LOG_DIR}/file.log
 
# # Copy and set permissions for the start1-up script
# COPY start1.sh /app/start1.sh
# RUN chmod +x /app/start1.sh
 
# # Expose ports (8000 for Daphne, other ports if necessary)
# EXPOSE 8004
 
# # Command to run the start1-up script
# CMD ["/app/start1.sh"]




# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir daphne celery

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variables
ENV MEDIA_ROOT=/home/ubuntu/media
ENV LOG_DIR=/app/logs

# Create directories for media files and logs
RUN mkdir -p ${MEDIA_ROOT} ${LOG_DIR}

# Create an empty log file
RUN touch ${LOG_DIR}/file.log

# Copy and set permissions for the startup script
COPY start1.sh /app/start1.sh
RUN dos2unix /app/start1.sh && chmod +x /app/start1.sh

# Expose ports (8004 for Daphne)
EXPOSE 8004

# Command to run the startup script
CMD ["/app/start1.sh"]

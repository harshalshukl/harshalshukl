# Use the official Python image.
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define the command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

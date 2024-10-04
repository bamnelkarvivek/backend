# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the service account JSON file into the container
COPY sturdy-filament-400423-9c0cb8a2379d.json /app/service_account.json

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask and Google Cloud authentication
ENV FLASK_APP=app.py
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/service_account.json

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

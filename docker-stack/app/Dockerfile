# Dockerfile for the app service

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the dashboard
EXPOSE 8050

# Command to run the application
CMD ["python", "main.py"]

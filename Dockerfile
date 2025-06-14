FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app to the container
COPY ./app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./app /app

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
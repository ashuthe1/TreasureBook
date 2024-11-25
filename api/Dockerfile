# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code and dependencies
COPY . /app
RUN pip install -r requirements.txt

# Expose API port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

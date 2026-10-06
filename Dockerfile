# Use official lightweight Python runtime
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first to take advantage of Docker layer caching
COPY requirements.txt .

# Install dependencies without cache to keep image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 3000 (matching the assignment port instructions)
EXPOSE 3000

# Run the Flask app
CMD ["python", "app.py"]

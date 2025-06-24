# Use official Python 3.10 slim image to avoid version conflicts
FROM python:3.10-slim

# Prevents Python from buffering stdout and stderr (makes logs visible immediately)
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy only requirements first for efficient caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy all your project files
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Start the Flask app with Gunicorn for production-grade server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

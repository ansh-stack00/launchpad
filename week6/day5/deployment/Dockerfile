# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

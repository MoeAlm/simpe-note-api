# Use an official Python runtime as a parent image
FROM python:3.12.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

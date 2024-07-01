FROM python:3.10.12

# Create and set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

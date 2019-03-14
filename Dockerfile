# Use an official Python runtime as a parent image
FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y python3-all-dev python3-venv postgresql-server-dev-all ca-certificates build-essential

RUN python3 -m venv /env

ENV PATH="/env/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install -U pip wheel

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN .

EXPOSE 8000

#CMD ["python3", "manage.py", "runserver"]

ENV PYTHONUNBUFFERED 1

# set base image (host OS)
FROM python:3.8
MAINTAINER Diego Costa <diegocostacmp@gmail.com>

RUN apt-get update && apt-get install -y build-essential python-dev
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-pip

# set the working directory in the container
ADD . /app
WORKDIR /app

# copy the dependencies and install
COPY requirements.txt .
RUN pip install -r requirements.txt


CMD ["python","app.py"]




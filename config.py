import os

from flask import Flask
from mongoengine import connect

app = Flask(__name__)

API_GET_PHISICIAN = os.environ.get("API_PHISICIAN")


mongo_url = "mongodb://localhost:27018/"
connect(db="iclinic-db-dev", host=mongo_url)

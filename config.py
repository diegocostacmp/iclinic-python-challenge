import os

from mongoengine import connect

API_GET_URL = os.environ.get("API_URL")
mongo_url = "mongodb://localhost:27017/"
db = connect(db="my-db", host=mongo_url)

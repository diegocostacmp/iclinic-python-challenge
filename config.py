import os

from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")
TOKEN_PHYSICIANS = os.getenv("TOKEN_PHYSICIANS")
TOKEN_CLINICS = os.getenv("TOKEN_CLINICS")
TOKEN_PATIENTS = os.getenv("TOKEN_PATIENTS")
TOKEN_METRICS = os.getenv("TOKEN_METRICS")
mongo_url = "mongodb://localhost:27017/"
db = connect(db="my-db", host=mongo_url)

from mongoengine import *


class PrescriptionModel(Document):
    clinic = IntField()
    physician = IntField(required=True)
    patient = IntField(required=True)
    text = StringField(max_length=500, required=True)

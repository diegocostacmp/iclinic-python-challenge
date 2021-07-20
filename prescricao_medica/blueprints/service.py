from flask import g
from requests import exceptions

from model import Prescription
from prescricao_medica.blueprints.errors import ERROR_007
from prescricao_medica.blueprints.restapi.resources import get_physician, post_metric


def build_prescription(data):
    """Consult dependents services,create item and send metric"""
    try:
        g.physician = get_physician(data["physician"]["id"])
        g.clinic = get_physician(data["clinic"]["id"])
        g.patient = get_physician(data["physician"]["id"])

        g.prescription = Prescription(
            clinic=int(g.clinic["id"]),
            physician=int(g.physician["id"]),
            patient=int(g.patient["id"]),
            text=data["text"],
        ).save()
        return True
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return ERROR_007


def build_metric():
    data_dict = {
        "clinic_id": g.clinic["id"],
        "clinic_name": g.clinic["name"] if g.clinic["name"] else None,
        "physician_id": g.physician["id"],
        "physician_name": g.physician["name"],
        "physician_crm": g.physician["crm"],
        "patient_id": g.patient["id"],
        "patient_name": g.patient["name"],
        "patient_email": g.patient["email"],
        "patient_phone": g.patient["phone"],
        "prescription_id": g.prescription.id,
    }
    g.metric, status = post_metric(data_dict)

    data_prescription = {
        "id": str(g.prescription.id),
        "clinic": {"id": g.clinic["id"]},
        "physician": {"id": g.physician["id"]},
        "patient": {"id": g.patient["id"]},
        "text": g.prescription.text,
        "metric": {"id": g.metric["id"]},
    }

    return data_prescription, True

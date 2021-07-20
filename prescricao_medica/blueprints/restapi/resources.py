from requests import get, exceptions, post
from config import (
    API_URL,
    TOKEN_PHYSICIANS,
    TOKEN_PATIENTS,
    TOKEN_METRICS,
    TOKEN_CLINICS,
)
from prescricao_medica.blueprints.errors import ERROR_005, ERROR_006, ERROR_004


def get_physician(physician_id: int):
    try:
        url = f"{API_URL}/physicians/{str(physician_id)}"
        physician = get(url=url, timeout=4, headers={"Authorization": TOKEN_PHYSICIANS})
        return physician.json()
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return ERROR_005


def get_clinic(clinic_id: int):
    try:
        url = f"{API_URL}/clinics/{str(clinic_id)}"
        clinic = get(url=url, timeout=4, headers={"Authorization": TOKEN_CLINICS})
        return clinic.json()
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return ERROR_005


def get_patient(patient_id):
    try:
        url = f"{API_URL}/patients/{str(patient_id)}"
        patient = get(url=url, timeout=4, headers={"Authorization": TOKEN_PATIENTS})
        return patient.json()
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return ERROR_006


def post_metric(data_dict):
    try:
        url = f"{API_URL}/metrics"
        metric = post(
            url, timeout=6, data=data_dict, headers={"Authorization": TOKEN_METRICS}
        )
        return metric.json(), True
    except exceptions.RequestException as e:
        print(f"Error: {e}")
        return ERROR_004

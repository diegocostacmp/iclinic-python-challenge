from integration import DependentServices
from model import PrescriptionModel

services_extras = DependentServices()


class PrescriptionService:
    def save_prescription(self, data):
        prescription = PrescriptionModel(
            clinic=int(data["clinic"]["id"]),
            physician=int(data["physician"]["id"]),
            patient=int(data["patient"]["id"]),
            text=data["text"],
        ).save()

        prescription_id = prescription.id
        request_updated = data.update({"id": prescription_id})

        return request_updated

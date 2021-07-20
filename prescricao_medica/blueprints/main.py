from flask import request, g

from app import app
from config import db
from prescricao_medica.blueprints.service import (
    build_prescription,
    build_metric,
)


@app.route("/prescriptions", methods=["POST"])
def prescription():
    save_prescription = False
    try:
        data_json = request.json
        clinic_id = data_json["clinic"].get("id")
        physician_id = data_json["physician"].get("id")
        patient_id = data_json["patient"].get("id")

        if not clinic_id:
            raise Exception("Error: Field clinid dont was informed")

        if not physician_id:
            raise Exception("Error: Field physician dont was informed")

        if not patient_id:
            raise Exception("Error: Field patient dont was informed")

        status_prescription = build_prescription(data_json)
        if status_prescription:
            save_prescription = True
    except Exception as e:
        save_prescription = False
        print(f"Error:{e}")
    finally:
        try:
            if save_prescription:
                data_prescription, status_metric = build_metric()
                if not status_metric:
                    prescription = db.prescription.find({"_id": g.prescription.id})
                    prescription.delete()
                return data_prescription
        except Exception as e:
            raise Exception(f"Has occurred a error when save DB. Error: {e}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

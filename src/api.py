from flask import request

from config import app
from service import PrescriptionService

prescription_service = PrescriptionService()


class PrescriptionApi:
    def __init__(self):
        self.trigger_endpoints()

    def trigger_endpoints(self):
        @app.route("/prescriptions", methods=["POST"])
        def create_prescription():
            try:
                save_prescription = True

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

            except Exception as e:
                save_prescription = False
                print(f"Error:{e}")

            finally:
                try:
                    if save_prescription:
                        return prescription_service.save_prescription(data_json)
                except Exception as e:
                    raise Exception(f"Has occurred a error when save DB. Error: {e}")

        @app.route("/metrics", methods=["POST"])
        def create_metric():
            try:
                save_metric = True

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

                prescription.validate_dependencies(data_json)

            except Exception as e:
                print(f"Error:{e}")

            finally:
                if save_metric:
                    # save DB
                    return


PrescriptionApi()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

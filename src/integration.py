from requests import get, post, exceptions
from config import API_GET_PHISICIAN

from errors import ERROR_005


class DependentServices:
    def get_physician(self, physician_id: int):
        try:
            url = f"{API_GET_PHISICIAN}{str(physician_id)}"
            phisician_result = get(url=url, timeout=4)

            return phisician_result
        except exceptions.RequestException as e:
            print(f"Error: {e}")
            return ERROR_005

    def get_clinics(self):
        return

    def get_patients(self):
        return

    def post_metrics(self):
        return

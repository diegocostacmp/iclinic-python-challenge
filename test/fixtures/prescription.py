from random import randint

import pytest
from faker import Faker

fake = Faker()


@pytest.fixture(scope="function")
def fixture_prescription_factory():
    def make(
        clinic: int = None,
        phisician: int = None,
        patient: int = None,
        prescription: str = None,
    ):
        clinic = clinic if clinic else randint(1, 50)
        phisician = phisician if phisician else randint(1, 50)
        patient = patient if patient else randint(1, 50)
        prescription = prescription if prescription else fake.text()

        return {
            "clinic": {"id": clinic},
            "physician": {"id": phisician},
            "patient": {"id": patient},
            "text": prescription,
        }

    yield make

import requests


def test_valid_post_prescription(fixture_prescription_factory):
    data_prescription = fixture_prescription_factory()
    headers = {
        "Content-Type": "application/json",
    }

    res = requests.post(
        "http://localhost:5000/prescriptions",
        json=data_prescription,
        headers=headers,
    )
    assert res.status_code == 200

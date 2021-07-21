import requests


def test_valid_post_prescription(fixture_prescription_factory):
    data_prescription = fixture_prescription_factory()
    headers = {
        "Content-Type": "application/json",
    }

    res = requests.post(
        "http://127.0.0.1:5000/api/prescriptions",
        json=data_prescription,
        headers=headers,
    )
    assert len(res.json()) == 6
    assert res.status_code == 200

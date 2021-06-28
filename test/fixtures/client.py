import pytest

from config import app


@pytest.fixture(scope="session")
def fixture_client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client

import pytest

from app import create_app

app = create_app()


@pytest.fixture(scope="session")
def fixture_client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

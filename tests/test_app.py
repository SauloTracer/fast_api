from fast_zero.app import app
from fastapi.testclient import TestClient
from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get("/")  # Act

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello -=FastApi"}

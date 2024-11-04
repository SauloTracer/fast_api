from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange

    response = client.get("/")  # Act

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello -=FastApi"}


def test_create_user_201_com_id_sem_password(client):
    response = client.post(
        "/users",
        json={
            "username": "test_user_name",
            "email": "test@test.com",
            "password": "password",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "test_user_name",
        "email": "test@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "test_user_name",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "test_user_name",
            "email": "test@test.com",
            "password": "#L3tm31n@fast_api",
            "id": 1,
        },
    )

    assert response.json() == {
        "username": "test_user_name",
        "email": "test@test.com",
        "id": 1,
    }


def test_user_not_found_put(client):
    response = client.put(
        "/users/99",
        json={
            "username": "test_user_name",
            "email": "test@test.com",
            "password": "#L3tm31n@fast_api",
            "id": 99,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User with id 1 deleted"}


def test_user_not_found_delete(client):
    response = client.delete("/users/99")

    assert response.status_code == HTTPStatus.NOT_FOUND

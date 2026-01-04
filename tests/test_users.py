from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ---------- WELCOME ----------
def test_welcome():
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my FastAPI app"}


# ---------- GET DEFAULT USER ----------
def test_get_default_user():
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json()["user_id"] == 1


# ---------- GET USER BY ID ----------
def test_get_user_by_id_success():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "person1"


def test_get_user_by_id_not_found():
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User with id 999 not found"


# ---------- CREATE USER ----------
def test_create_user_success():
    payload = {
        "name": "person2",
        "user_id": 2,
        "title": "devops engineer",
        "email_address": "person2@xyz.com"
    }

    response = client.post("/user", json=payload)
    assert response.status_code == 201
    assert response.json()["user_id"] == 2


def test_create_user_conflict():
    payload = {
        "name": "person1",
        "user_id": 1,
        "title": "infra engineer",
        "email_address": "person1@xyz.com"
    }

    response = client.post("/user", json=payload)
    assert response.status_code == 409


# ---------- UPDATE USER ----------
def test_update_user_success():
    payload = {
        "name": "person1_updated",
        "user_id": 1,
        "title": "platform engineer",
        "email_address": "person1@xyz.com"
    }

    response = client.put("/user/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "platform engineer"


# ---------- DELETE USER ----------
def test_delete_user_success():
    response = client.delete("/user/2")
    assert response.status_code == 204


def test_delete_user_not_found():
    response = client.delete("/user/999")
    assert response.status_code == 404

import string
import random

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_signup_existing_user():
    response = client.post("/signup", json={"username": 'test', "password": 'test'})
    assert response.status_code == 200
    assert response.json() == {"message": "User already exists!"}


def test_signup_new_user():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    response = client.post("/signup", json={"username": random_string, "password": random_string})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully!"}


def test_login_correct_credentials():
    response = client.post("/login", json={"username": "testuser12", "password": "testuser12"})
    assert response.status_code == 200
    assert response.json()["message"] == "Logged in successfully!"
    assert "access_token" in response.json()
    assert "access_token" != ""


def test_wrong_password():
    response = client.post("/login", json={"username": "testuser12", "password": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "Could not log in. Wrong Password!", "access_token": ""}


def test_non_existing_user_login():
    response = client.post("/login", json={"username": "testuser1233", "password": "testuser1233"})
    assert response.status_code == 200
    assert response.json() == {"message": "User does not exist!", "access_token": ""}


def test_products_list():
    response = client.get("/products")
    assert response.status_code == 200
    assert type(response.json()) == list
    for i in response.json():
        assert type(i) == dict
        assert len(i) == 5

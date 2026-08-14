"""
Test suite for the ReqRes Users API.
Covers positive, negative, and edge case scenarios for GET and POST endpoints.

Run with: pytest test_users.py -v
"""

import requests
from config import BASE_URL, HEADERS




# ---------- GET /users ----------

def test_get_users_list_returns_200():
    """TC01: Retrieving a list of users should return 200 and a non-empty list."""
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
    assert response.status_code == 200

    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


def test_get_single_existing_user_returns_correct_data():
    """TC02: Retrieving an existing user should return correct fields."""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200

    user = response.json()["data"]
    assert user["id"] == 2
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user


def test_get_nonexistent_user_returns_404():
    """TC03: Requesting a user that doesn't exist should return 404."""
    response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS)
    assert response.status_code == 404


# ---------- POST /users ----------

def test_create_user_with_valid_data_returns_201():
    """TC04: Creating a user with valid data should return 201 and echo the data back."""
    payload = {"name": "Vuyiswa", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201

    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body


def test_create_user_with_empty_payload():
    """TC05: Creating a user with an empty payload should still respond gracefully (no server error)."""
    response = requests.post(f"{BASE_URL}/users", json={}, headers=HEADERS)
    # ReqRes is a mock API and doesn't enforce required fields,
    # so we check it doesn't fail with a 5xx server error.
    assert response.status_code < 500


# ---------- POST /register ----------

def test_register_with_valid_credentials_returns_token():
    """TC06: Registering with valid email and password should return a token."""
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()


def test_register_with_missing_password_returns_400():
    """TC07: Registering without a password should fail with a clear error."""
    payload = {"email": "eve.holt@reqres.in"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 400
    assert "error" in response.json()


# ---------- PUT /users ----------

def test_update_user_returns_updated_at():
    """TC08: Updating an existing user should return 200 with an updatedAt timestamp."""
    payload = {"name": "Vuyiswa", "job": "Senior QA Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "updatedAt" in response.json()


# ---------- DELETE /users ----------

def test_delete_user_returns_204():
    """TC09: Deleting an existing user should return 204 No Content."""
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 204


# ---------- Edge case: response time ----------

def test_get_user_response_time_is_acceptable():
    """TC10: API should respond within an acceptable threshold (2 seconds)."""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.elapsed.total_seconds() < 2
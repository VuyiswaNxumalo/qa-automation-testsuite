
import requests
 
BASE_URL = "https://reqres.in/api"
 
 
# ---------- POST /login ----------
 
def test_login_with_valid_credentials_returns_token():
    """TC11: Logging in with valid credentials should return a token."""

    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
 
 
def test_login_with_missing_email_returns_400():
    """TC12: Logging in without an email should fail with a clear error."""

    payload = {"password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"
 
 
def test_login_with_invalid_email_format():
import requests
 
BASE_URL = "https://reqres.in/api"
 
 
# ---------- POST /login ----------
 
def test_login_with_valid_credentials_returns_token():
    """TC11: Logging in with valid credentials should return a token."""
    
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
 
 
def test_login_with_missing_email_returns_400():
    """TC12: Logging in without an email should fail with a clear error."""
    payload = {"password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"
 
 
def test_login_with_invalid_email_format():
    """TC13: Logging in with a malformed email should still be handled gracefully
    (no 5xx server error), even though this mock API doesn't validate format."""
    payload = {"email": "not-an-email", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code < 500
 
    """TC13: Logging in with a malformed email should still be handled gracefully
    (no 5xx server error), even though this mock API doesn't validate format."""
    payload = {"email": "not-an-email", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code < 500
 
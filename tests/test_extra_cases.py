import requests
from config import BASE_URL, HEADERS
 
 
 
#POST /login
 
def test_login_with_valid_credentials_returns_token():
    """TC11: Logging in with valid credentials should return a token."""
    
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()
 
 
def test_login_with_missing_email_returns_400():
    """TC12: Logging in without an email should fail with a clear error."""
    
    payload = {"password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"
 
 
def test_login_with_invalid_email_format():
    """TC13: Logging in with a malformed email should still be handled gracefully
    (no 5xx server error), even though this mock API doesn't validate format."""

    payload = {"email": "not-an-email", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code < 500
 
    """TC13: Logging in with a malformed email should still be handled gracefully
    (no 5xx server error), even though this mock API doesn't validate format."""

    payload = {"email": "not-an-email", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code < 500
 

#Pagination edge cases 
 
def test_get_users_page_zero_does_not_error():
    """TC14: Requesting page 0 (invalid page number) should not cause a server error."""
    response = requests.get(f"{BASE_URL}/users?page=0", headers=HEADERS)
    assert response.status_code == 200
 
 
def test_get_users_high_page_number_returns_empty_data():
    """TC15: Requesting a page far beyond available data should return
    a 200 with an empty data list, not an error."""
    response = requests.get(f"{BASE_URL}/users?page=9999", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["data"] == []
 
 
#Invalid data types
 
def test_get_user_with_non_numeric_id_returns_404():
    """TC16: Requesting a user with a non-numeric ID should return 404,
    not a server crash."""
    response = requests.get(f"{BASE_URL}/users/abc", headers=HEADERS)
    assert response.status_code == 404
 
 
def test_create_user_with_wrong_data_type_for_name():
    """TC17: Sending a number instead of a string for 'name' should still
    be handled without a server error (documents API's leniency)."""
    payload = {"name": 12345, "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code < 500
 
 
#Delayed response endpoint 
 
def test_delayed_response_still_returns_200():
    """TC18: The delayed response endpoint should eventually return 200,
    confirming the client handles slower responses correctly."""
    response = requests.get(f"{BASE_URL}/users?delay=3", headers=HEADERS, timeout=10)
    assert response.status_code == 200
    assert "data" in response.json()
 
 
def test_delayed_response_within_reasonable_timeout():
    """TC19: A delayed response should still complete within a generous
    timeout threshold, flagging potential performance issues otherwise."""
    response = requests.get(f"{BASE_URL}/users?delay=3", headers=HEADERS, timeout=10)
    assert response.elapsed.total_seconds() < 10
 
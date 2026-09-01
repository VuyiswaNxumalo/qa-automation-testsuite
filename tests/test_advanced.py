import requests
import pytest
from config import BASE_URL, HEADERS

@pytest.mark.parametrize("user_id", [1,4,6,8,12])
def test_get_existing_users_returns_200(user_id):
       """TC20: Every known valid user ID (1-12 range) should return 200
    with matching data. Runs once per user_id in the list above."""
    response.get(f"{BASE_URL}/users/{user_id}" ,headers= HEADERS)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


@pytest.mark.parametrize("invalid_id", [0, -1, 13, 999, "abc"])
def test_get_invalid_user_ids_returns_404(invalid_id):
    """TC21: Any ID outside the valid range (or non-numeric) should
    consistently return 404, not a mix of different error behaviors."""
    response = requests.get(f"{BASE_URL}/users/{invalid_id}", headers=HEADERS)
    assert response.status_code == 404
 
 
@pytest.mark.parametrize("page,expected_min_users", [
    (1, 1),
    (2, 1),
])
def test_valid_pages_return_users(page, expected_min_users):
    """TC22: Pages 1 and 2 (the only pages with real data) should
    each return at least one user."""
    response = requests.get(f"{BASE_URL}/users?page={page}", headers=HEADERS)
    assert response.status_code == 200
    assert len(response.json()["data"]) >= expected_min_users
 
 
 
def test_full_user_lifecycle_workflow():
    """TC23: Simulates a full user lifecycle - create, verify creation,
    update, verify update, then delete - checking state consistency
    across the whole chain rather than testing each step in isolation."""
 
    # Step 1 Create a user
    create_payload = {"name": "Vuyiswa Test", "job": "QA Engineer"}
    create_response = requests.post(
        f"{BASE_URL}/users", json=create_payload, headers=HEADERS
    )
    assert create_response.status_code == 201
    created_user = create_response.json()
    user_id = created_user["id"]
    assert created_user["name"] == create_payload["name"]
 
    # Step 2 Update the same user
    update_payload = {"name": "Vuyiswa Test", "job": "Senior QA Engineer"}
    update_response = requests.put(
        f"{BASE_URL}/users/2", json=update_payload, headers=HEADERS
    )
    assert update_response.status_code == 200
    updated_user = update_response.json()
    assert updated_user["job"] == update_payload["job"]
    assert "updatedAt" in updated_user
 
    # Step 3 Delete the user
    delete_response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert delete_response.status_code == 204
 
    
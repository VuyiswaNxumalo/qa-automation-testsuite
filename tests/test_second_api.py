"""
Test suite for JSONPlaceholder (https://jsonplaceholder.typicode.com) -
a second, unrelated public API, added to demonstrate that the testing
approach used for ReqRes transfers to a different API with a different
shape and no authentication requirement.

Run with: pytest test_second_api.py -v
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts_returns_200():
    """TC24: Retrieving all posts should return 200 and a non-empty list."""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


def test_get_single_existing_post_returns_correct_fields():
    """TC25: Retrieving an existing post should return the expected fields."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

    post = response.json()
    assert post["id"] == 1
    assert "title" in post
    assert "body" in post
    assert "userId" in post


def test_get_nonexistent_post_returns_404():
    """TC26: Requesting a post that doesn't exist should return 404."""
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404

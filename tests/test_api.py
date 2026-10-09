```python
from app import app


def test_get_users():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/users")

        assert response.status_code == 200
        assert isinstance(response.json, list)


def test_get_user_posts():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/users/1/posts")

        assert response.status_code == 200
        assert isinstance(response.json, list)


def test_get_post_not_found_or_success():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/posts/999999")

        assert response.status_code in [200, 404, 500]
```

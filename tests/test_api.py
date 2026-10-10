
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


def test_get_post_not_found():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/posts/999999")

        assert response.status_code == 404


def test_create_post():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/posts",
            json={
                "title": "My First Post",
                "content": "This is my test post",
                "user_id": 1
            }
        )

        assert response.status_code == 201
        assert response.json["message"] == "Post created"
        assert "id" in response.json

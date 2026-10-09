from app import app


def test_get_users():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/users")

        assert response.status_code == 200
        assert isinstance(response.json, list)

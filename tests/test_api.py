
import pytest

from app import create_app, db


@pytest.fixture
def client():
    test_app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
    })

    with test_app.app_context():
        db.drop_all()
        db.create_all()

        from app.models.user import User

        user = User(name="Test User", age=25)
        db.session.add(user)
        db.session.commit()

        yield test_app.test_client()

        db.session.remove()
        db.drop_all()


def test_get_users(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_user_posts(client):
    response = client.get("/users/1/posts")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_post_not_found(client):
    response = client.get("/posts/999999")

    assert response.status_code == 404


def test_create_post(client):
    response = client.post(
        "/posts",
        json={
            "title": "My First Post",
            "content": "This is my test post",
            "user_id": 1,
        },
    )

    assert response.status_code == 201
    assert response.json["message"] == "Post created"
    assert "id" in response.json

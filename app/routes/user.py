```python
from flask import Blueprint, request

from app.services.user_services import (
    create_user,
    get_all_users,
    update_user,
    delete_user
)

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users():
    users = get_all_users()

    return [
        {
            "id": user.id,
            "name": user.name,
            "age": user.age
        }
        for user in users
    ]


@users_bp.route("/users", methods=["POST"])
def create_user_route():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    if "name" not in data or "age" not in data:
        return {"error": "Name and age are required"}, 400

    if not isinstance(data["name"], str) or not data["name"].strip():
        return {"error": "Name must be a non-empty string"}, 400

    if isinstance(data["age"], bool) or not isinstance(data["age"], int):
        return {"error": "Age must be an integer"}, 400

    if data["age"] < 0:
        return {"error": "Age cannot be negative"}, 400

    user = create_user(
        data["name"].strip(),
        data["age"]
    )

    return {
        "message": "User created",
        "id": user.id
    }, 201


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    if "name" not in data or "age" not in data:
        return {"error": "Name and age are required"}, 400

    if not isinstance(data["name"], str) or not data["name"].strip():
        return {"error": "Name must be a non-empty string"}, 400

    if isinstance(data["age"], bool) or not isinstance(data["age"], int):
        return {"error": "Age must be an integer"}, 400

    if data["age"] < 0:
        return {"error": "Age cannot be negative"}, 400

    user = update_user(
        user_id,
        data["name"].strip(),
        data["age"]
    )

    if user is None:
        return {"error": "User not found"}, 404

    return {
        "message": "User updated",
        "id": user.id
    }, 200


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    user = delete_user(user_id)

    if user is None:
        return {"error": "User not found"}, 404

    return {
        "message": "User deleted successfully"
    }, 200
```

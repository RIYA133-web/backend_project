from flask import Blueprint, request

from app.models.user import User
from app import db

from app.services.user_services import (
    create_user,
    get_all_users,
    update_user
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
    data = request.json

    user = create_user(
        data["name"],
        data["age"]
    )

    return {
        "message": "User created",
        "id": user.id
    }, 201


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.json

    user = update_user(
        user_id,
        data["name"],
        data["age"]
    )

    return {
        "message": "User updated",
        "id": user.id
    }

from flask import Blueprint, request

from app import db
from app.models.user import User
from app.services.post_services import (
    create_post,
    get_post,
    get_user_posts
)

posts_bp = Blueprint("posts", __name__)


@posts_bp.route("/posts", methods=["POST"])
def create_post_route():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Request body must be valid JSON"}, 400

    required_fields = ["title", "content", "user_id"]

    for field in required_fields:
        if field not in data:
            return {"error": f"Missing required field: {field}"}, 400

    if not isinstance(data["title"], str) or not data["title"].strip():
        return {"error": "Title must be a non-empty string"}, 400

    if not isinstance(data["content"], str) or not data["content"].strip():
        return {"error": "Content must be a non-empty string"}, 400

    if not isinstance(data["user_id"], int) or isinstance(data["user_id"], bool):
        return {"error": "user_id must be an integer"}, 400

    user = db.session.get(User, data["user_id"])

    if user is None:
        return {"error": "User not found"}, 404

    post = create_post(
        data["title"],
        data["content"],
        data["user_id"]
    )

    return {
        "message": "Post created",
        "id": post.id
    }, 201


@posts_bp.route("/posts/<int:post_id>", methods=["GET"])
def get_post_route(post_id):
    post = get_post(post_id)

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "user_id": post.user_id
    }


@posts_bp.route("/users/<int:user_id>/posts", methods=["GET"])
def get_user_posts_route(user_id):
    posts = get_user_posts(user_id)

    return [
        {
            "id": post.id,
            "title": post.title,
            "content": post.content
        }
        for post in posts
    ]
    

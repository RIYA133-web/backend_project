from flask import Blueprint, request

from app.services.post_service import (
    create_post,
    get_post,
    get_user_posts
)

posts_bp = Blueprint("posts", __name__)


@posts_bp.route("/posts", methods=["POST"])
def create_post_route():
    data = request.json

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
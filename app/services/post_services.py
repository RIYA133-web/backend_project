from app.models.post import Post
from app import db


def create_post(title, content, user_id):
    post = Post(
        title=title,
        content=content,
        user_id=user_id
    )

    db.session.add(post)
    db.session.commit()

    return post


def get_post(post_id):
    return Post.query.get_or_404(post_id)


def get_user_posts(user_id):
    return Post.query.filter_by(user_id=user_id).all()
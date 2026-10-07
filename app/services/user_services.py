from app.models.user import User
from app import db


def create_user(name, age):
    user = User(
        name=name,
        age=age
    )

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():
    return User.query.all()


def update_user(user_id, name, age):
    user = User.query.get_or_404(user_id)

    user.name = name
    user.age = age

    db.session.commit()

    return user
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from app.models.user import User
    from app.models.post import Post

    with app.app_context():
        db.create_all()

    from app.routes.user import users_bp
    from app.routes.post import posts_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)

    return app


app = create_app()

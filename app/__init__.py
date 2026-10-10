
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


from app.models.user import User
from app.models.post import Post


with app.app_context():
    db.create_all()


from app.routes.user import users_bp
from app.routes.post import posts_bp

app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

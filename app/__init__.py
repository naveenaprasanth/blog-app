from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    with app.app_context():
        from app import models
        db.create_all()

    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.posts import posts
    from app.routes.admin import admin

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(posts)
    app.register_blueprint(admin)

    return app


from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
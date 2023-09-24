from flask import Flask
from config import Config
from app.extentions import db, migrate, jwt, login_manager
from app.auth import authBp
from app.post import postBp

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(authBp, url_prefix="/api/auth")
    app.register_blueprint(postBp, url_prefix="/api/post")

    return app

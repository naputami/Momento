from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_login import LoginManager
from minio import Minio

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()
client = Minio("play.minio.io:9000", access_key="Q3AM3UQ867SPQQA43P2F", secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG")

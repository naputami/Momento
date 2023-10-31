from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_login import LoginManager
from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()
client = Minio(f'{os.getenv("MINIO_URL")}', access_key=f'{os.getenv("MINIO_ACCESS_KEY")}', secret_key=f'{os.getenv("MINIO_SECRET_KEY")}', secure=False)

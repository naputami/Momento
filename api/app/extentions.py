from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_login import LoginManager
from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD")
MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER")
MINIO_URL = os.getenv("MINIO_URL")

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()
client = Minio(        
        MINIO_URL, 
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False
        )

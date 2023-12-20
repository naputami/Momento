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
        "play.min.io", 
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        )

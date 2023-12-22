import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()


class Config:
    POSTGRES_USER = os.getenv(POSTGRES_USER)
    POSTGRES_DB = os.getenv(POSTGRES_DB)
    POSTGRES_PASSWORD = os.getenv(POSTGRES_PASSWORD)
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}?charset=utf8mb4'.format(POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_USER,POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESG_TOKEN_EXPIRES = timedelta(days = 30)
    FLASK_ADMIN_SWATCH = 'pulse'
    SECRET_KEY = os.getenv('SECRET_KEY')


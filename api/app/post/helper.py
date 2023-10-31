import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_EXTENTION = {"jpg", "png", "jpeg"}
BUCKET_NAME = os.getenv('MINIO_BUCKET')

def allowed_file(filename):
    filename = filename.lower()
    extention = filename.split(".")[-1]
    return extention in ALLOWED_EXTENTION
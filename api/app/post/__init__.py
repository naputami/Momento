from flask import Blueprint
from flask_cors import CORS

postBp = Blueprint("post", __name__)
CORS(postBp)
from app.post import routes
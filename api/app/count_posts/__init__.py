from flask import Blueprint
from flask_cors import CORS

countPostBp = Blueprint('countPost', __name__)
CORS(countPostBp)

from app.count_posts import routes
from sanic import Blueprint
from routes import v1

api = Blueprint.group(v1.index, url_prefix='/v1')
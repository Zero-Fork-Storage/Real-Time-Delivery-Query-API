from sanic.blueprints import Blueprint
from sanic.response import json
from sanic import response

from routes.v1.index_root import api_info

index = Blueprint.group(api_info)
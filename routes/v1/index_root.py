from sanic.blueprints import Blueprint
from sanic.response import json
from sanic import request

import platform
import sys

api_info = Blueprint('v1.api_info')

# API Information /v1/index
@api_info.route('/index')
async def ApiV1root(request):
	os_version = platform.system() + " " + str(platform.version())
	return json(
		{
			"msg": "Hello",
			"API_info": [
				{
					"PROJECT_VERSION": "1.0",
					"python_version": sys.version,
					"OS": os_version
				}
			]
		}
	)
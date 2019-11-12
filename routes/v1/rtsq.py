from controllers.utils.rtsq_templit import gen
from sanic.blueprints import Blueprint
from sanic.response import json
from sanic.response import text
from sanic import response
from sanic import request

rtsq_Api = Blueprint('v1.rtsq')


@rtsq_Api.route('/rtsq', methods=["POST"])
async def RtsqApi(request):
	if request.method != 'POST':
		msg = f"Method {request.method} not allowed for URL {request.url}"
		return json(
			{
				"Exception": msg
			},
			status=405
		)

	if request.json is None:
		msg_c = {
			"Exception": "Request None"
		}
		return json(msg_c)


	json_data = request.json

	name = json_data['name']
	code = json_data['code']

	resp = gen(name=name, t_invoice=code)
	return json(
		resp,
		status=200
	)
from typing import Dict, Any, Union

from controllers.utils.rtsq_library.rtsq_array import arrayConverter
from controllers.utils.rtsq_library.rtsq_level import level
from controllers.utils.rtsq_library.dst_co import Code
from controllers.utils.test import rtsq

import json

def gen(name, t_invoice):
	res: Dict[str, Union[Optional[str], Any]] = {
		'itemName': '알 수 없음',
		'phone': '010-0000-0000',
		'where': '알 수 없음',
		'time': '알 수 없음',
		'manName': '알 수 없음',
		'estimate': '알 수 없음',
		'status': '알 수 없음',
	}

	t_code = Code.search(name=name)
	resp = rtsq.get(t_code, t_invoice)

	try:
		if resp['tracking_info']['ErrorMsg']:
			print("Error")
			if resp['tracking_info']['ErrorMsg'] == "not isValidInvoice":
				return {
					'ErrorType': 'not is Valid Invoice',
					'ErrorCode': resp['tracking_info']['ErrorCode']
				}
			else:
				return {
					'ErrorType': resp['tracking_info']['ErrorMsg'],
					'ErrorCode': resp['tracking_info']['ErrorCode']
				}
	except KeyError as ex:
		print('No Error')
		pass

	if resp is None:
		print('Cannot get Response.')
		return res

	result = resp['result']

	if result != "Y":
		print('Cannot get Response.')
		return res

	lv = level(resp)

	if lv['code'] == 0:
		print('Internal Server Error')
		print(level(resp))
		return {
			res,
			{
				"Error": "Internal Server Error"
			}
		}


	res['estimate'] = resp['estimate']

	if 6 == lv['code']:
		res['itemName'] = None
		res['phone'] = None
		res['time'] = resp['lastStateDetail']['timeString']
		res['where'] = resp['lastStateDetail']['where']
		res['manName'] = resp['lastStateDetail']['manName']
		res['status'] = resp['lastStateDetail']['kind']

		return {
			'now': res,
			'history': arrayConverter(resp)
		}

	if 1 > lv['code'] > 5:
		res['itemName'] = resp["itemName"]
		res['phone'] = resp["trackingDetails"][lv['code']]["telno"]
		res['time'] = resp["trackingDetails"][lv['code']]["timeString"]
		res['where'] = resp["trackingDetails"][lv['code']]["where"]
		res['manName'] = resp["trackingDetails"][lv['code']]["manName"]
		res['status'] = resp["trackingDetails"][lv['code']]["kind"]

		return {
			'now': res,
			'history': arrayConverter(resp)
		}

	return res

print(json.dumps(gen(name="CJ대한통운", t_invoice="0000000000"), indent=4, ensure_ascii=False))
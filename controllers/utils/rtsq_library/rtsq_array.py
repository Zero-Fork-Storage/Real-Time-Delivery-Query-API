def arrayConverter(resp):
	c_rex = []
	for item in resp["trackingDetails"]:
		trackingDetails = {
			'timeString': item['timeString'], 'where': item['where'],
			'manName': item['manName'], 'telno': None,
			'kind': None, 'status': item['kind']
		}
		c_rex.append(trackingDetails)
	return c_rex

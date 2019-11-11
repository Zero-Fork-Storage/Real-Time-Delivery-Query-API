def level(resp):
	"""
	Args:
		resp:

	level:
		string

	Returns:
		[level 1: 배송준비중, 2: 집화완료, 3: 배송중, 4: 지점 도착, 5: 배송출발, 6:배송 완료]
	"""

	if resp['level'] == 1:
		return {
			"code": 1,
			"level": "배송 준비중"
		}

	elif resp['level'] == 2:
		return {
			"code": 2,
			"level": "집화 완료"
		}

	elif resp['level'] == 3:
		return {
			"code": 3,
			"level": "배송중"
		}

	elif resp['level'] == 4:
		return {
			"code": 4,
			"level": "지점 도착"
		}

	elif resp['level'] == 5:
		return {
			"code": 5,
			"level": "배송 출발"
		}

	elif resp['level'] == 6:
		return {
			"code": 6,
			"level": "배송 완료"
		}

	else:
		return {
			"code": 0,
			"level": "Internal System Error"
		}

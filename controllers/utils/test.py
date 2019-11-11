from fake_useragent import UserAgent
import requests
import json


class Rtsq:
	def __init__(self):
		self.Apiuri = "http://rest.sweettracker.net/tracking"
		self.t_key = "SWEETTRACKER"

	def get(self,  t_code, t_invoice):
		ua = UserAgent()
		headers = {
			"User-Agent": ua['google chrome']
		}

		req = requests.get(self.Apiuri, headers=headers, params={
			"t_key": self.t_key,
			"t_code": t_code,
			"t_invoice": t_invoice
		})

		if req.status_code != 200:
			print('Can get rtsq.')
			return None

		return req.json()

rtsq = Rtsq()

from fake_useragent import UserAgent
import requests
import asyncio
import aiohttp
import json
import nest_asyncio
nest_asyncio.apply()

class rtsq:
    def __init__(self, t_code, t_invoice):
        self.parms = {"t_key": "SWEETTRACKER", "t_code": t_code, "t_invoice": t_invoice}


    async def rtsq_base(self):
        ua = UserAgent()
        headers = {
            "User-Agent": ua['google chrome']
        }

        Apiuri = "http://rest.sweettracker.net/tracking"
        async with aiohttp.ClientSession() as session:
            async with session.get(Apiuri, params=self.parms, headers=headers) as resp:
                return await resp.json()


#print(rtsq_get(t_code="04", t_invoice="0000000000").getrtsq())

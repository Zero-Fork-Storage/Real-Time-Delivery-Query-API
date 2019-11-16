Real-Time Delivery Query API
====
![pythonVersion](https://img.shields.io/badge/python-v3.7-blue) ![License](https://img.shields.io/badge/License-MIT-blue)\
Real-Time Delivery Query API provides fast response speed by applying asynchronous programming, \
and provides processed and processed JSON with better readability than existing delivery tracking API.

## Prerequisites
 - Python 3.7 +
 - sanic
 - aiohttp
 - nest_asyncio

## Usage
**1. Install prerequisites**
```sh
1. $ pip install -r requirements.txt
2. $ pip3 install -r requirements.txt
4. $ python3 -m pip install -r requirements.txt
```

**2. Run**
```bash
python3 server-run.py
```

**3. How to use**
- HTTP
```HTTP
POST /v1/rtsq HTTP/1.1
Content-Type: application/json
{
	"name": "CJ대한통운",
	"code": "0000000000"
}
```
---
- curl
```github
curl -X POST \
  http://127.0.0.1:8000/v1/rtsq \
  -H 'Content-Type: application/json' \
  -d '{
	"name": "CJ대한통운",
	"code": "0000000000"
}'
```
- node js
```javascript
var request = require("request");

var options = { method: 'POST',
  url: 'http://127.0.0.1:8000/v1/rtsq',
  headers: {'Content-Type': 'application/json' },
  body: { name: 'CJ대한통운', code: '0000000000' },json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

## Author
 - Euiseo Cha (차의서) | zeroday0619 : \
    [Github](https://github.com/zeroday0619) \
    [Facebook](https://www.facebook.com/EuiseoCha) \
    [Tistory | 티스토리 블로그](https://blog.zeroday0619.kr/)

## LICENSE
Copyright 2019 Euiseo Cha (차의서) | zeroday0619 \
[MIT License](https://github.com/zeroday0619/Real-Time-Delivery-Query-API/blob/master/LICENSE)

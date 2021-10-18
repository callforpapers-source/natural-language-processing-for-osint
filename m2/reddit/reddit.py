
import requests
import json
# Missed
from requests import Timeout

q = 'owasp'
limit = 250

url = 'https://api.pushshift.io/reddit/comment/search'
params = {
	'q': q,
	'html_decode': True,
	'size': 100
}

grabbed = 0
comments = []

while grabbed <= limit:
	try:
		req = requests.get(url, params=params)
	except Timeout:
		print('retrying...')
	except Exception as e:
		print('Connection Error', e)
	else:
		print(grabbed)
		data = req.json()['data']
		grabbed += len(data)
		comments.extend(data)
		params['before'] = data[-1]['created_utc']


json.dump([x['body'] for x in comments], open('outcome.json', 'w'), indent=4)


import requests
from requests.exceptions import Timeout
import json


q = "Trump"
limit = 500
headers = {
	'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
	'x-twitter-client-language': 'en'
}

get_token = 'https://api.twitter.com/1.1/guest/activate.json'
search_url = 'https://twitter.com/i/api/2/search/adaptive.json'

params = {
	'q': q,
	'count': 20,
	'simple_quoted_tweet': True,
	'query_source': 'typed_query'
}

for _ in range(3):
	try:
		req = requests.post(get_token, headers=headers, timeout=10)
		break
	except Timeout:
		print('retrying...')
	except Exception as e:
		print('Connection error', e)
else:
	exit()

headers['x-guest-token'] = req.json()['guest_token']
print(headers)

tweets = []
page = 0

while page*20 < limit:
	try:
		req = requests.get(search_url, headers=headers, params=params, timeout=10)
	except Timeout:
		print('retrying...')
	except Exception as e:
		print('Connection error', e)
	else:
		page += 1
		resp = req.json()
		instruct = resp['timeline']['instructions']
		get_cursor_value = lambda x: x['content']['operation']['cursor']['value']
		if page == 1:
			params['cursor'] = get_cursor_value(instruct[0]['addEntries']['entries'][-1])
		else:
			params['cursor'] = get_cursor_value(instruct[-1]['replaceEntry']['entry'])

		fresh_tweets = resp['globalObjects']['tweets']
		tweets.extend([fresh_tweets[x].get('text') for x in fresh_tweets])
		print(len(tweets))


json.dump(tweets, open('results.json', 'w'))


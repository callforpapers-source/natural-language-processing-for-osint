
import requests
from requests.exceptions import Timeout
import json


q = "chess until:2021-02-01 since:2021-01-01"
limit = 100
headers = {
	'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
	'x-twitter-client-language': 'en'
}

get_token = 'https://api.twitter.com/1.1/guest/activate.json'
search_url = 'https://twitter.com/i/api/2/guide.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&count=20&candidate_source=trends&include_page_configuration=false&entity_tokens=false&ext=mediaStats%2ChighlightedLabel%2CvoiceInfo'


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

for _ in range(3):
	try:
		req = requests.get(search_url, headers=headers, timeout=10)
	except Timeout:
		print('retrying...')
	except Exception as e:
		print('Connection error', e)
	else:
		page = req.json()
		break
else:
	exit()


json.dump(page, open('results.json', 'w'), indent=4)
results = page['timeline']['instructions'][1]['addEntries']['entries'][1]['content']['timelineModule']['items']
trends = {}
for i in results:
	i = i['item']['content']['trend']
	name = i['name']
	metadata = i.get('trendMetadata')
	trends[name] = [name]
	if metadata:
		trends[name].append(metadata.get('metaDescription') or 'none')
		trends[name].append(metadata['domainContext'])

print(trends)
print(len(trends))

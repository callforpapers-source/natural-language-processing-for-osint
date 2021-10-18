
from lxml import html
import requests
import json
from urllib import parse

url = 'https://pubmed.ncbi.nlm.nih.gov'

root = '//article'
a = './/a[@class="docsum-title"]'
authors = '//span[@class="docsum-authors full-authors"]'
citation = '//span[@class="docsum-journal-citation full-journal-citation"]'
snip = '//div[@class="full-view-snippet"]'

query = "biochemical"
count = 200
params = {'term': query, 'size': count}
page = ''


print(f'Searching...')
try:
	req = requests.get(url, params=params)
except Exception as e:
	raise e
else:
	page += req.text

tree = html.fromstring(page)
results = tree.xpath(root)
outcome = []

for i in results:
	result = {}
	link = i.xpath(a)
	result['href'] = parse.urljoin(url, link[0].get('href'))
	result['title'] = link[0].text_content().strip()
	result['authors'] = i.xpath(authors)[0].text_content().strip()
	result['citation'] = i.xpath(citation)[0].text_content().strip()
	result['content'] = i.xpath(snip)[0].text_content().strip()
	outcome.append(result)
	print(result)
	print('\n')

json.dump(outcome, open('results.json', 'w'))
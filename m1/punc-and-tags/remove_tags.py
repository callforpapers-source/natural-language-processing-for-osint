import requests
from bs4 import BeautifulSoup as bs
import re

text = requests.get('https://gnu.org').text

def strip_tags(html):
	soup = bs(html, 'html.parser')
	strip = soup.get_text()
	return strip

def remove_puncs(text):
	remove_punc3 = r"[^A-z0-9 ]+"
	text = re.sub(remove_punc3, ' ', text)
	text = re.sub(r'[\s]+', ' ', text)
	return text

print(remove_puncs(strip_tags(text)))

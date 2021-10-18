
import joblib
import json
import doc2term
import re

model = joblib.load('HS.joblib')

dataset = json.loads(open('trump.json').read())
tweets = []
for i in dataset:
	clean_tweets = [re.sub(r"\[|\]|'", '', doc2term.doc2term_str(x).replace('.', '')).lower() for x in dataset[i]]
	tweets.extend(clean_tweets)

predicted = model.predict(tweets)

print((sum(predicted)/len(tweets))*100)

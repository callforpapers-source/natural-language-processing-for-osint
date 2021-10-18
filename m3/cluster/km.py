import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
from nltk.corpus import stopwords
import re

def rstopwords(doc, without_punc=True):
	doc = doc.lower()
	stops = stopwords.words('english')
	if without_punc:
		to_punc = punc(doc).split()
	else:
		to_punc = doc.split()
	return ' '.join([x for x in to_punc if x not in stops])

def punc(doc):
	replace = re.sub(r"[\W]+", " ", doc)
	return " ".join(replace.split())

def euclidean_distance(x, y):
	return np.sqrt(np.sum((x - y) ** 2))

def cosine_similarity(x,y):
	return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

doc1 = rstopwords(open('ML.txt').read())
doc2 = rstopwords(open('DL.txt').read())
doc3 = rstopwords(open('MJ.txt').read())
doc4 = rstopwords(open('AI.txt').read())


TV = TfidfVectorizer()

data = TV.fit_transform([doc1, doc2, doc3, doc4]).todense()
data = np.array(data)

km = KMeans(n_clusters=3)
km.fit(data)

print(km.labels_)

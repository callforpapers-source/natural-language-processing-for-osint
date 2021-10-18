import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
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
	return [x for x in to_punc if x not in stops]

def punc(doc):
	replace = re.sub(r"[\W]+", " ", doc)
	return " ".join(replace.split())

def euclidean_distance(x, y):
	return np.sqrt(np.sum((x - y) ** 2))

def cosine_similarity(x,y):
	return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

doc1 = open('ML.txt').read()
doc2 = open('DL.txt').read()
doc3 = open('MJ.txt').read()
doc4 = open('AI.txt').read()

query = 'natural language processing'
query1 = 'cannabis is a kind of flower'

CV = TfidfTransformer()
TV = TfidfVectorizer()

data = CV.fit_transform([doc1, doc2, doc3, doc4, query, query1]).todense()

data = np.array(data)


print('ML - DL', cosine_similarity(data[0], data[1]))
print('ML - MJ', cosine_similarity(data[0], data[2]))
print('ML - AI', cosine_similarity(data[0], data[3]))
print('DL - MJ', cosine_similarity(data[1], data[2]))
print('DL - AI', cosine_similarity(data[1], data[3]))
print('AI - MJ', cosine_similarity(data[2], data[3]))
print('ML - query1', cosine_similarity(data[0], data[4]))
print('ML - query2', cosine_similarity(data[0], data[5]))
print('DL - query1', cosine_similarity(data[1], data[4]))
print('DL - query2', cosine_similarity(data[1], data[5]))
print('MJ - query1', cosine_similarity(data[3], data[4]))
print('MJ - query2', cosine_similarity(data[3], data[5]))
print('AI - query1', cosine_similarity(data[2], data[4]))
print('AI - query2', cosine_similarity(data[2], data[5]))

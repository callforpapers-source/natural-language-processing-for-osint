import numpy as np

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

doc1 = rstopwords(open('ML.txt').read().lower())
doc2 = rstopwords(open('DL.txt').read().lower())
doc3 = rstopwords(open('MJ.txt').read().lower())
doc4 = rstopwords(open('AI.txt').read().lower())

query = 'computer'

vectors = open('glove.6B.100d.txt').read().split('\n')
model = {}

for i in vectors:
	i = i.split(' ')
	model[i[0]] = np.array([float(x) for x in i[1:]])

def measure_distance_between_q_doc(q, doc):
	qm = model[q]
	nofk = len(doc)
	sigma = 0
	for i in doc:
		if i in model:
			sigma += cosine_similarity(qm, model[i])
		else:
			nofk -= 1

	sigma /= nofk
	sigma *= 100
	return sigma

print(measure_distance_between_q_doc(query, doc1))
print(measure_distance_between_q_doc(query, doc2))
print(measure_distance_between_q_doc(query, doc3))
print(measure_distance_between_q_doc(query, doc4))
print()
print(measure_distance_between_q_doc('addict', doc1))
print(measure_distance_between_q_doc('addict', doc2))
print(measure_distance_between_q_doc('addict', doc3))
print(measure_distance_between_q_doc('addict', doc4))

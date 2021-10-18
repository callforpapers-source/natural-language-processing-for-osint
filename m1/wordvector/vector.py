from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

text = [open('text2-phrase').read()]
text = ['there is no time for us as it is for other', 'time is everything', 'time does not have direction', 'time goes everywhere like a particle']
vectorizer = CountVectorizer()
vectorizer = TfidfVectorizer()
vectorizer.fit(text)

vectors = vectorizer.transform(text)

# print(vectorizer.idf_)
print(vectors)
print(vectorizer.vocabulary_)
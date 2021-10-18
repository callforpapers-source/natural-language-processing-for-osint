from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

# print(TextBlob(text).ngrams(3))

text = ["I am going to learn NLP and I am passionate about Y"]
vectorizer = CountVectorizer(ngram_range=(2,2))
vectorizer.fit(text)
vector = vectorizer.transform(text)
print(vectorizer.vocabulary)
print(vector)
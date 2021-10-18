# import json
from collections import Counter
# from doc2term import doc2term_str
# import re
# import unicodedata
# from nltk.corpus import stopwords
# from spacy import load

# ////////// text1

# stop_words = open('our_stopwords').read().split()
# file = json.loads(open('trump.json').read())

# corpus = ''

# for i in file:
# 	corpus += ' '.join(file[i])

# corpus = unicodedata.normalize('NFKD', corpus).encode('ascii', 'ignore').decode('u8', 'ignore')
# corpus = doc2term_str(corpus)
# corpus = re.sub(r'[\. \[\]]+', ' ', corpus)
# corpus = re.sub(r'[\s]+', ' ', corpus)
# open('text1', 'w').write(corpus)

# /////////////// text2


# corpus = open('text1').read().lower()
# corpus = corpus.split(' ')
# # remove stop words
# corpus = [x for x in corpus if x not in stop_words]
# open('text2_without_stopwords_lower', 'w').write(' '.join(corpus))


# ////////// text3

# corpus = open('text2_without_stopwords_lower').read().lower()
# corpus = corpus.split(' ')

# nlp = load('en_core_web_sm')
# corpus = nlp(corpus)
# # lemmatization
# corpus = [x.lemma_ for x in corpus]
# open('text3_lemm', 'w').write(' '.join(corpus))


# ////////// bag of words for wordcloud

# from wordcloud import WordCloud
# from matplotlib import pyplot as plt

# corpus = open('text2-phrase').read().lower()
# corpus = corpus.split(' ')
# bow = Counter(corpus)
# # print(bow.most_common(50))

# cloud_data = ' '.join([x for x in corpus if '_' in x])
# plt.imshow(WordCloud().generate(cloud_data), interpolation='bilinear')
# plt.axis('off')
# plt.title('election')
# plt.show()

# //////////// bag of words for histogram

from matplotlib import pyplot as plt
import pandas as pd


corpus = open('text2-phrase').read().lower()
corpus = corpus.split(' ')
bow = Counter([x for x in corpus if '_' in x])

dataframe = pd.DataFrame(bow.most_common(100), columns=('words', 'frequency'))

fig, ax = plt.subplots(figsize=(25,25))

dataframe.sort_values(by='frequency').plot.barh(x='words', y='frequency', ax=ax, color='black')

ax.set_title('election')

plt.show()
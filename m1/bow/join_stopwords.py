from nltk.corpus import stopwords
stop_words = stopwords.words('english')

more = open('extra_stopwords').read().split()
stop_words.extend(more)
stop_words = list(set(stop_words))
open('our_stopwords','w').write('\n'.join(stop_words))
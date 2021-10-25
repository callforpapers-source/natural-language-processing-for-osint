
import pandas as pd
import re
# In the video we imported test.csv but there is no need to do so. You can use train data for training as well as testing.
from sklearn.utils import resample
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from joblib import load,dump

# Remove usernames and meaningless characters and links
def preproc(data_frame, tweet_field):
	data_frame[tweet_field] = data_frame[tweet_field].str.lower()
	data_frame[tweet_field] = data_frame[tweet_field].apply(lambda x: re.sub(r"(@[\w]+)|([^0-9A-z \t])|(\w+:\/\/\S+)|^rt|http.+?", '', x))
	return data_frame


train = pd.read_csv('train.csv')
# test = pd.read_csv('test.csv')
print("Training set", train.columns, ',', train.shape)
# print("Test set", test.columns, ',', test.shape)

train = preproc(train, 'tweet')
# test = preproc(test, 'tweet')

train_maj = train[train.label == 0]
train_min = train[train.label == 1]

train_min_upsampled = resample(train_min, replace=True, n_samples=len(train_maj), random_state=99)

train_subsampled = pd.concat([train_min_upsampled, train_maj])

print(train_subsampled['label'].value_counts())

SGD = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('nb', SGDClassifier())])

X_train, X_test, Y_train, Y_test = train_test_split(train_subsampled['tweet'], train_subsampled['label'], random_state=0)

model = SGD.fit(X_train, Y_train)
y_predict = model.predict(X_test)
print(f1_score(Y_test, y_predict))

print(model.predict(["no comment  in australia   opkillingbay seashepherd helpcovedolphins thecove helpcovedolphins", "how dumb ass you are"]))

dump(model, 'HS.joblib')

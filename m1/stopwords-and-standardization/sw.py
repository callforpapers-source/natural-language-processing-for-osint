
from nltk import corpus
from doc2term import doc2term_str
import re

stopwords = corpus.stopwords.words('english')

text = """As an example, an introductory course focusing on logic, set theory, and real analysis might cover
Lessons 1, 2, 5, 9, 10, and 13. Lessons 1 and 9 cover basic sentential logic and proof theory, Lessons 2
and 10 cover basic set theory including relations, functions, and equinumerosity, and Lessons 5 and 13
cover basic real analysis up through a rigorous treatment of limits and continuity. The first three lessons
are quite basic, while the latter three lessons are at an intermediate level. Instructors that do not like
the idea of leaving a topic and then coming back to it later can cover the lessons in the following order
without issue: 1, 9, 2, 10, 5, and 13.ةةةة
"""

text = [x for x in re.split(r'[\. \n]', doc2term_str(text.lower())) if x != '']

new = []
for i in text:
	if i not in stopwords:
		new.append(i)

print(' '.join(new))

# abbrs = {"isn't": 'is not', "you'll": 'you will', 'nlp': 'natural language processing', 'ml': 'machine learning', "couldn't": 'could not', 'temp.': 'temperature'}

# for i in text:
# 	if i in abbrs:
# 		new.append(abbrs[i])
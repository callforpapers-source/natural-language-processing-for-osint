
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import re
from Stemmer import Stemmer

text = """As an example, an introductory course focusing on logic, set theory, and real analysis might cover
Lessons 1, 2, 5, 9, 10, and 13. Lessons 1 and 9 cover basic sentential logic and proof theory, Lessons 2
and 10 cover basic set theory including relations, functions, and equinumerosity, and Lessons 5 and 13
cover basic real analysis up through a rigorous treatment of limits and continuity. The first three lessons
are quite basic, while the latter three lessons are at an intermediate level. Instructors that do not like
the idea of leaving a topic and then coming back to it later can cover the lessons in the following order
without issue: 1, 9, 2, 10, 5, and 13.ةةةة
"""

# stemmer = PorterStemmer()
# stemmer = LancasterStemmer()

# text = re.sub(r'[^A-z ]+', ' ', text)
# text = re.sub(r'[ \t\n]+', ' ', text)
# split = text.lower().split(' ')
# new = []
# for i in split:
# 	x = stemmer.stem(i)
# 	print(i, ' => ', x)
# 	new.append(x)

# print(' '.join(new))


# ////////////

stemmer = Stemmer('english')

print(stemmer.stemWords('As an example an introductory course focusing on logic set theory and real analysis might cover Lessons'.lower().split(' ')))
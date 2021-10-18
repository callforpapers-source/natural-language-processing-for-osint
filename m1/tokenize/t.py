from nltk import sent_tokenize, word_tokenize
from doc2term import doc2term_str
import nltk
import re

text = """As an example, an introductory course focusing on logic, set theory, and real analysis might cover
Lessons 1, 2, 5, 9, 10, and 13. Lessons 1 and 9 cover basic sentential logic and proof theory, Lessons 2
and 10 cover basic set theory including relations, functions, and equinumerosity, and Lessons 5 and 13
cover basic real analysis up through a rigorous treatment of limits and continuity. The first three lessons
are quite basic, while the latter three lessons are at an intermediate level. Instructors that do not like
the idea of leaving a topic and then coming back to it later can cover the lessons in the following order
without issue: 1, 9, 2, 10, 5, and 13, i.e p, q domain.com and xyz@abc.def 2008.01.10 file.txt https://url.com .ةةةة
"""

# a = sent_tokenize(text)
# print(a)
# print(len(a))
# b = doc2term_str(text, include_numbers_dates=1, include_emails_phones_urls=1, include_hosts_files=1)
# print(b)
# print(len(b.split(' . ')))

# print(word_tokenize(text))

# print([x.split(' ') for x in b.split(' . ')])

# treebank = nltk.TreebankWordTokenizer()
# print(treebank.tokenize(text))


# print(re.split(r'[^A-z\.\-0-9]+', text))
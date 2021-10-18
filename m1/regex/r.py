import re

text = """As an example, an introductory course focusing on logic, set theory, And real analysis might cover
Lessons 1, 2, 5, 9, 10, and 13. Lessons 1 and 9 cover basic sentential logic and proof theory, Lessons 2 
and 10 cover basic set theory including relations, functions, and equinumerosity, and Lessons 5 and 13
cover basic real analysis up through a rigorous treatment of limits and continuity. The first three lessons
are quite basic, while the latter three lessons are +_)(*&^%$#@!<>?at an intermediate level. Instructors that do not like
the idea of leaving a topic and then coming back to it later can cover the lessons in the following order
without issue: 1, 9, 2, 10, 5, and 13.ةةةة
# xyz@abc.de
# x-y1z@a.bc.de

# xyz@bbbb.bcde
# xyz@.a
# xyz@-a.com
"""


email = r"([A-z\-\.0-9]+@[A-z0-9]{1}[A-z0-9\-\.]+)|([A-z\-\.0-9]+@[A-z0-9\-\.]+)"

# https://google.com/abc?q=3
# http://www.google.com/abc?q=3
# ftp://www.google.com/abc

# xyz@abc.de
# x-y1z@a.bc.de

# xyz@bbbb.bcde
# xyz@.a
# xyz@-a.com

re.search
re.findall
re.compile
re.sub
re.split

# print(re.split(r"[0-9]+[0-9, ]+", text))
# print(re.sub(r"[^A-z0-9]+", ' ', text)))

email = re.compile(email)
# print(email.match("xyz@.bcde"))
# print(email.findall(text))
# print(re.findall(email, text))
# print(re.search(email, text))
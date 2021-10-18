
import re


text = """As an example, an introductory course focusing on logic, set theory, and real analysis might cover
Lessons 1, 2, 5, 9, 10, and 13. Lessons 1 and 9 cover basic sentential logic and proof theory, Lessons 2
and 10 cover basic set theory including relations, functions, and equinumerosity, and Lessons 5 and 13
cover basic real analysis up through a rigorous treatment of limits and continuity. The first three lessons
are quite basic, while the latter three lessons are at an intermediate level. Instructors that do not like
the idea of leaving a topic and then coming back to it later can cover the lessons in the following order
without issue: 1, 9, 2, 10, 5, and 13.ةةةة
"""

remove_punc1 = r"[^\w ]+"
remove_punc2 = r"[\.\-,;:?!]+"
remove_punc3 = r"[^A-z0-9 ]+"

text = re.sub(remove_punc2, '', text)
print(text)
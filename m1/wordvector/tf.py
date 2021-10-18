from collections import Counter

text = open('text2-phrase').read().split(' ')

tf = {}
bow = Counter(text)
for i in bow:
	tf[i] = bow[i]/len(bow)

print(tf['election'])
print(tf['trump'])
print(tf['vote'])
print(tf['biden'])
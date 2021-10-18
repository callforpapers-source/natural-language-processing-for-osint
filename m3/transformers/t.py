from transformers import pipeline

model = pipeline('sentiment-analysis')
print(model('it could be good'))

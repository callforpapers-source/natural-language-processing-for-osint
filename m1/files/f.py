
# import PyPDF2
# from PyPDF2 import PdfFileReader
# import textract

# pdf = open('pdf.pdf', 'rb')

# reader = PyPDF2.PdfFileReader(pdf)
# print(reader.numPages)
# first_page  = reader.getPage(2)

# print(first_page.extractText())

# /////////

# text = textract.process('pdf.pdf', method='pdfminer')
# print(text)

# ///////////

# import json

# json.dumps()
# json.dump({'hi': 'there'}, open('test.json', 'w'), indent=4)
# x = json.dumps("{'hi': 'there'}")
# y = json.loads(open('test.json').read())
# print(y['hi'])

# /////////

# import csv

# reader = csv.reader(open('test.csv'), delimiter=',')
# for i in reader:
# 	print(i)

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import json
import csv
from PyPDF2 import PdfFileReader


driver = webdriver.Chrome()
file = open('Data Engineer Task - Data Engineer Task.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)
print(rows)
pdfFileObject = open(pdf_path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
pdf_extract = ''
for row in rows:
    driver.get(row)
    pdf_path= row
    for i in range(0,pdfReader.numPages):

        # creating a page object
        pageObj = pdfReader.getPage(i)
        # extracting text from page
        text=text+pageObj.extractText()


json_object = json.loads(text)
with open("pdf_extract.json", "w") as outfile:
    outfile.write(json_object)




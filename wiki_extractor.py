from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

keyword = input()
num_urls = int(input())
result = requests.get("https://en.wikipedia.org/wiki/" + keyword)
source = result.content
driver = webdriver.Chrome()
soup = bs(source, 'html.parser')
links = soup.find_all("a")
print(links)

urls = []
for link in links:
    
    url = link.get('href')
    if url and "/wiki/" in url:
        urls.append("https://en.wikipedia.org" + url)
        urls.append(url)

for url in urls[1:num_urls]:
    if url and "https://" in url:
        texts = driver.find_element("body")
        print(texts.text)

#It is working up till here, some Chromedirver verison issues have arised which is causing trouble, need time to resolve that. 
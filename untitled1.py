from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome= webdriver.Chrome()

chrome.get("")

time.sleep(3)

for i in range(5):
    chrome.execute_script('')
    time.sleep(1)
    
soup = BeautifulSoup((chrome.page_source),"html.parser")

for each_prod in soup.find_all('h5', class_="prod_name"):
    
    
chrome.close()
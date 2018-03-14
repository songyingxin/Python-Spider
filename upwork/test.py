import os
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://www.upwork.com/fl/sorin")
time.sleep(10)
file = open('test.html','w')
file.write(driver.page_source)
driver.close()

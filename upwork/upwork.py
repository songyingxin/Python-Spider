from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.upwork.com/o/profiles/users/_~01eae6bcdb295209de/")
soup = BeautifulSoup(driver.page_source.encode('UTF-8'),'lxml')
hourly = soup.find('span',itemprop="pricerange").get_text()
print(hourly)
driver.close()

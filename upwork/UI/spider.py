from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pymongo

def get_content(url,driver):
    driver.get(url)
    return BeautifulSoup(driver.page_source.encode('UTF-8'),'lxml')






if __name__ == '__main__':
    start_url = 'https://www.upwork.com/o/profiles/browse/c/web-mobile-software-dev/sc/web-mobile-design/fb/45/?page='
    end_url = '&q=UI%2FUX'
    home_url = start_url + str(1) + end_url
    driver = webdriver.Chrome()
    soup = get_content(home_url, driver)
    print(soup.prettify())

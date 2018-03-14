from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.upwork.com/o/profiles/users/_~01eae6bcdb295209de/")
soup = BeautifulSoup(driver.page_source.encode('UTF-8'),'lxml')
name = soup.find('span',itemprop="name").get_text()
locality = soup.find('span', itemprop="locality").get_text()
country = soup.find('strong', itemprop="country-name").get_text()

success_rate = soup.find('h3',class_="m-0-bottom ng-binding").get_text()

hourly_rate = soup.find('span',itemprop="pricerange").get_text()
con = soup.find_all('li', class_="width-xs m-0-bottom ng-scope")

total_earn = soup.find('li',class_="width-xs m-lg-right m-0-bottom ng-scope").find('span',itemprop="pricerange").get_text()
jobs = soup.find_all('li', class_="width-xs m-0-bottom ng-scope")[0].find('h3', class_="m-xs-bottom ng-binding").get_text()
work_jours = soup.find_all('li', class_="width-xs m-0-bottom ng-scope")[1].find('h3', class_="m-xs-bottom ng-binding").get_text()


#print(hourly_rate + name + locality + country + success_rate + total_earn + jobs + work_jours)
# 不能爬尽所有技能
skills = []
skills_all = soup.find('div', class_="o-profile-skills m-sm-top ng-scope")
print(skills_all)
'''
for item in skills_all:
    skill = item.get_text()
    print(skill)
'''

driver.close()

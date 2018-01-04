# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup


url = 'https://www.upwork.com/o/profiles/users/_~01f99f991bf49a923b/'


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
headers = {
    'User-Agent': user_agent
}

try:
    response = requests.get(url, headers=headers)
except requests.ConnectionError as e:
    print('遇见网络问题')
except requests.HTTPError as e:
    print('HTTP请求返回不成功的状态码')
except requests.Timeout as e:
    print('请求超时')
except requests.TooManyRedirects as e:
    print('太多的重定向次数')
except requests.exceptions.RequestException as e:
    print('请求错误，未知异常')

soup = BeautifulSoup(response.text,'lxml')
item1 = soup.find("div",id='optimizely-header-container-default')
#locality = item1.find("span",class_="text-capitalize ng-binding").string
#contry = item1.find("strong",itemprop='country-name').string

#success = item1.find("h3",class_="m-0-bottom ng-binding").string

#hourly_rate = item1.find("span", itemprop="pricerange").string
print(item1)

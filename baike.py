# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup

page = 1
bash_url = 'https://www.qiushibaike.com/text/page/'
start_url = bash_url + str(page) + '/'

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
headers = {
    'User-Agent': user_agent
}

try:
    response = requests.get(start_url, headers=headers)
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


content = response.text
soup = BeautifulSoup(content,'lxml')
items = soup.find("div",id='content-left',class_='col1').find_all("div",class_=re.compile("article block untagged mb15 typs_long|hot|old"))

for item in items:
    name = item.find("h2").string
    text = item.find("div",class_="content").get_text()
    laugh_num = item.find("span",class_="stats-vote").i.string
    comment_num = item.find("a",class_="qiushi_comments").i.string
    print(name,text,laugh_num,comment_num)

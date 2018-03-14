# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/text/page/1/'   # 要爬取的url

#请求头部
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
headers = {
    'User-Agent': user_agent
}

response = requests.get(url, headers=headers)    # 请求网页获取响应报文

content = response.text
soup = BeautifulSoup(content,'lxml')   # 解析HTML文本
# 获取每个笑话，一个item代表一个笑话
items = soup.find("div",id='content-left',class_='col1').find_all("div",
             class_=re.compile("article block untagged mb15 typs_long|hot|old"))

for item in items:
    name = item.find("h2").string   # 获取作者名字
    text = item.find("div",class_="content").get_text()    # 获取笑话内容
    laugh_num = item.find("span",class_="stats-vote").i.string    # 获取点赞数
    comment_num = item.find("a",class_="qiushi_comments").i.string   # 获取评论数
    print(name,text,laugh_num,comment_num)

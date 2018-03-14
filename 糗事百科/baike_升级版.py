# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup

class spider_baike:
    '''
    对糗事百科进行爬取的爬虫，主要实现单一页面的爬取，没有深入递归爬取与多页面爬取

    Attributes:
        user_agent: 上文有说哦
        headers: 请求头部
        base_url: 你应该懂
    '''

    def __init__(self):
        '''
        初始化变量
        '''
        self.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        self.headers = {'User-Agent': self.user_agent}
        self.base_url = 'https://www.qiushibaike.com/text/page/'

    def get_page(self,page=1):
        '''
        获取页面的HTML文本
        '''
        try:
            url = self.base_url + str(page) + '/'
            response = requests.get(url, headers=self.headers)
            return response
        except requests.ConnectionError as e:
            print('遇见网络问题')
            return None
        except requests.HTTPError as e:
            print('HTTP请求返回不成功的状态码')
            return None
        except requests.Timeout as e:
            print('请求超时')
            return None
        except requests.TooManyRedirects as e:
            print('太多的重定向次数')
            return None
        except requests.exceptions.RequestException as e:
            print('请求错误，未知异常')
            return None

    def get_items(self,page=1):
        '''
        提取HTML文本中的item并以字符串的形式输出
        '''
        result_items = []
        response = self.get_page(page)

        content = response.text
        soup = BeautifulSoup(content,'lxml')
        items = soup.find("div",id='content-left',class_='col1').find_all("div",class_=re.compile("article block untagged mb15 typs_long|hot|old"))
        for item in items:
            name = item.find("h2").string)
            text = item.find("div",class_="content").get_text()
            laugh_num = item.find("span",class_="stats-vote").i.string
            comment_num = item.find("a",class_="qiushi_comments").i.string
            result_item = [name,text,laugh_num,comment_num]
            result_items.append(result_item)
        return result_items


if __name__ == '__main__':
    spider = spider_baike()
    result = spider.get_items(1)
    for item in result:
        print('作者为: {}'.format(item[0]))
        print('点赞数为：{}'.format(item[2]))
        print('评论数为：{}'.format(item[3]))
        print('内容为：{} \n\n\n'.format(item[1]))

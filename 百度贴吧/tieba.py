import requests
import re
from bs4 import BeautifulSoup

class spider_tieba:
    '''
    对百度贴吧进行爬取的爬虫
    '''
    def __init__(self,base_url):
        self.base_url = base_url

    def get_page(self, page_mun=1):
        '''
        获取该页帖子的HTML文本
        '''
        try:
            payload = {'pn': page_mun,'see_lz': 1}
            response = requests.get(url=self.base_url,params=payload)
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


    def get_title(self):
        '''
        获取百度贴吧帖子的标题
        这篇帖子的标题为：IU-Ready『同款』130723◇妹纸的同款【不定期更新】
        '''
        page = self.get_page(1)
        soup = BeautifulSoup(page.text,'lxml')
        title = soup.find("h1",class_='core_title_txt').string
        if title:
            return str(title)
        else:
            print('提取失败')
            return NOne
    def get_total_num(self):
        '''
        获取该帖子的总页数
        Attribute: 无
        '''
        page = self.get_page(1)
        soup = BeautifulSoup(page.text,'lxml')
        total_num = soup.find("li",class_='l_reply_num').find_all('span',class_='red')[1].string

        if total_num:
            return int(total_num)
        else:
            print('提取失败')
            return None

    def get_content(self,page_num=1):
        '''
        获取帖子的内容
        Attribute:
        page_num: 要爬取的帖子页数，默认为1
        '''
        page = self.get_page(page_num)
        soup = BeautifulSoup(page.content,'lxml')
        contents = soup.find_all('div',class_="d_post_content j_d_post_content  clearfix")

        floor = 1   # 几楼的帖子，以便后期核对
        result = ''   # 结果作为字符串返回

        for content in contents:
            content = content.get_text()
            result += str(floor) + ':' + content + "\n"
            floor += 1

        return result


def main():
    spider =  spider_tieba('http://tieba.baidu.com/p/2477816287')
    html = spider.get_page()    # 获取百度贴吧的HTML文本
    title = spider.get_title()    # 获取帖子标题
    total_num = spider.get_total_num()    # 获取帖子页数

    page_num = 1
    result = ''
    while page_num <= total_num:
        result += "第" + str(page_num) + "层的数据" + "\n" + spider.get_content(page_num) + "\n\n\n"
        page_num += 1
    print(result)

    # 将文本写入到output.txt文件中，此处我就不进行封装了，不要太简单
    file = open("output.txt","w")
    file.write(result)
    file.close()

if __name__ == '__main__':
    main()

import os
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

class ClassTaoBaoSpider(object):

    """
    用于爬取淘宝MM的相关信息

    Attributes:
        driver: 使用selenium的浏览器实例
        url： 根url
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_content(self,url):
        """
        获取该网页中的HTML文本，并使用Beautiful解析
        返回值： Beautiful解析后的文本
        """
        if url is None:
            print('url is None, can\'t spider')

        self.driver.get(url)   # 访问网站
        time.sleep(2)
        soup = BeautifulSoup(self.driver.page_source,'lxml')
        #self.driver.close()
        return soup


    def get_info(self, soup):
        """
        获取淘宝MM的姓名，城市，体重，身高，点赞数
        Attributes:
            soup: Beautifulsoup解析后的文本
        """

        if soup is None:
            print("没有获取到解析后的文本")
            return None
        items = soup.find_all('li', class_="item")  # 获取所有MM相关HTML

        if items is None:
            print("查找失败")
            return None

        contents = []   # 用列表存储淘宝MM的信息

        '''
        提取淘宝MM的相关信息
        '''
        for item in items:
            name = item.find('span',class_="name").get_text()  #姓名
            city = item.find('span',class_="city").get_text()  # 居住城市
            wei_hei = item.find('div',class_="info row2").span.get_text()
            weight = re.compile(r'[0-9]{3}CM').findall(wei_hei)[0] #体重
            height = re.compile(r'[0-9]{2}KG').findall(wei_hei)[0]  #身高
            like = item.find('span',class_="fr").get_text()[1:]  #喜欢数
            link = item.find('a',class_="item-link")['href']  #个人主页链接

            contents.append([link,name,city,weight,height,like])
        return contents

    def get_pictures(self, contents):
        '''
        爬取第一页中所有MM的图片
        Attributes:
            contents: get_info()中返回的值
        '''
        if contents is None:
            print('参数为None')
            return None

        '''
        循环访问每个MM的主页，并将主页中所有照片保存到当前文件夹中
        '''
        for content in contents:

            dir_name = '.' + os.sep + content[1]  # 以MM名字作为文件夹名
            if os.path.exists(dir_name) is False:
                os.makedirs(dir_name)

            MM_url = "https:" + content[0]   # MM 的主页url
            soup = self.get_content(MM_url)   # 获取MM主页的 HTML 代码
            pic_urls = soup.find_all("img",src=re.compile(".*?.jpg"))   # 获取MM主页中的所有图片链接
            num = 0   # 以数字区分图片名

            print("正在爬取" + content[1] + "的图片： ")

            for pic_url in pic_urls:
                img_url = pic_url["src"]
                if not img_url.startswith("http"):
                    img_url = "http:" + img_url # https也行

                print("正在获取" + content[1] + '的第' + str(num) + "张图片")
                self.save_picture(img_url,num,dir_name)
                num += 1

    def save_picture(self, url, num, dir_name):
        '''
        保存一张图片
        Attributes
            url: 图片的Url
            num: 为了唯一识别图片，以数字命名图片
            dir_name: 图片保存的文件夹
        '''

        if url is None:
            print('url is None,can\'t save')
            return

        file_name = dir_name + os.sep + str(num)+'.jpg' # 文件名
        if os.path.exists(file_name):
            return
        '''
        保存图片
        '''
        try:
            response = requests.get(url)
            file = open(file_name,'wb')
            file.write(response.content)
            print('save picture' + str(num))
        except Exception as e:
            print('save picture exception' + str(e))

def main():
    home_url = "https://mm.taobao.com/search_tstar_model.htm?spm=719.7763510.1998606017.2.Z9fHzT"   # 根url
    driver = webdriver.PhantomJS()
    spider = ClassTaoBaoSpider(driver,home_url)
    soup = spider.get_content(home_url)
    contents = spider.get_info(soup)
    #print(contents)
    spider.get_pictures(contents)
    driver.close()

if __name__ == '__main__':
    main()

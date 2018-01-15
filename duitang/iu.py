import json
import os
import re
import requests

class ClassIUSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'www.duitang.com',
            'Referer': 'https://www.duitang.com/search/?kw=iu&type=feed',
            'Accept': 'application/json, text/javascript',
        }


    def get_json(self,start,id):
        '''
        获取一个包含JSON数据的url的内容
        Attributes
            start: 表示该Url中的一个变量，star
            id: 表示该Url中的另一个变量
        '''

        url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=iu&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&_type=&start=' + str(start) + '&_=' + str(id)   # 注意，start，id为int型，此处要转换为字符串
        print(url)        # 输出此时的Url，一遍后续输出时判断你下载的是哪个Url中的图片

        '''
        使用requests库获取该Url中包含的JSON格式的数据
        此处将所有的异常都囊括了
        '''
        try:
            response = requests.get(url)
            return response.text
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


    def get_urls(self,content):
        '''
        获取JSON数据中的图片的Url
        Attributes
            content: 表示Json数据， 为response.text
        '''

        if content is None:
            return None
        try:
            '''
            获取该JSON数据中包含的所有图片Url，并将其存储到一个列表中
            '''
            data_list = json.loads(content)['data']['object_list']  # 解析json数据，一般从网络中获取的json数据都需要解析
            url_lsit = []
            for data in data_list:
                url_lsit.append(data['photo']['path'])
        except Exception as e:
            print('json 解析失败' + str(e))
        return url_lsit


    def save_picture(self, url, num):
        '''
        保存一张图片
        Attributes
            url: 图片的Url
            num: 为了唯一识别图片，以数字命名图片
        '''

        if url is None:
            print('url is None,can\'t save')
            return
        dir_name = '.' + os.sep + 'iu'    # 保存图片的目录名
        if os.path.exists(dir_name) is False: # 创建目录
            os.makedirs(dir_name)
        file_name = dir_name + '/' + str(num)+'.png' # 文件名
        if os.path.exists(file_name):
            return
        try:
            '''
            保存图片
            '''
            response = requests.get(url)
            file = open(file_name,'wb')
            file.write(response.content)
            print('save picture' + str(num))
        except Exception as e:
            print('save picture exception' + str(e))

    def scraw_all(self,start=0,id=1515327378056,end=1515327378070):
        '''
        开始保存所有图片
        Attributes:
            start: url中的变量
            id: url中的变量
            end: 爬取终止条件
        '''
        num = 0    # 用于图片的文件名，唯一
        origin_start = start
        origin_id = id
        end_id = end

        while(origin_id <= end_id ):
            content = self.get_json(origin_start,origin_id)
            origin_id += 1
            origin_start += 24
            urls = self.get_urls(content)
            for url in urls:
                self.save_picture(url,num)
                num += 1


def main():
    spider = ClassIUSpider()
    spider.scraw_all(0,1515327378056,1515327378070)

if __name__ == '__main__':
    main()

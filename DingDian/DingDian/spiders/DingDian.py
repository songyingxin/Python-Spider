import re
from bs4 import BeautifulSoup
import scrapy
from scrapy.http import Request
from DingDian.items import DingdianItem

class DingDianSpider(scrapy.Spider):
    name = "DingDian"
    allowed_domains = ["23us.so"]
    base_url = "http://www.23us.so/list/"
    end_url = ".html"

    def start_requests(self):

        for i in range(1, 2):   # 如果要爬取所有分类的话，更改此处即可
            url = self.base_url + str(i) + "_1" + self.end_url
            #print("这是我们的根url: " + url)
            yield Request(url, self.parse)


    def parse(self, response):
        end_page = "10"
        #end_page = BeautifulSoup(response.text, "lxml").find("a",class_="last").get_text()  # 页数
        base_url = str(response.url)[:-6]   # 各个页之间共性的url
        for page in range(1, int(end_page)+1):
            url = base_url + str(page) + self.end_url
            #print(" 玄幻页面的所有URL: " + url)
            yield Request(url, self.get_url)

    def get_url(self,response):
        """
        获取小说的url
        """
        contents = BeautifulSoup(response.text, "lxml").find_all("tr", bgcolor="#FFFFFF")  # 寻找所有的小说框
        for content in contents:
            name = content.find("td").a.get_text()   # 小说名字
            url = content.a["href"]    # 小说url
            yield Request(url, self.get_items)
    def get_items(self, response):
        """
        获取所有的item
        """
        item = DingdianItem()
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find("table", id="at")
        contents = table.find_all("td")

        item["category"] = contents[0].get_text()
        item["author"] = contents[1].get_text()
        item["status"] = contents[2].get_text()

        item["star_num"] = contents[3].get_text()
        item["char_num"] = contents[4].get_text()
        item["last_update"] = contents[5].get_text()

        item["total_click_num"] = contents[6].get_text()
        item["month_click_num"] = contents[7].get_text()
        item["week_click_num"] = contents[8].get_text()

        item["total_recommend"] = contents[9].get_text()
        item["month_recommend"] = contents[10].get_text()
        item["week_recommend"] = contents[11].get_text()
        print(item["category"], item["author"] , item["status"], item["star_num"], item["char_num"],item["last_update"],
             item["total_click_num"],item["month_click_num"],item["week_click_num"],item["total_recommend"],
              item["month_recommend"],item["week_recommend"])

        yield item

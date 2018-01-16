# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 小说类别，小说作者，小说状态
    category = scrapy.Field()
    author = scrapy.Field()
    status = scrapy.Field()

    # 收藏数，全文长度，最后更新
    star_num = scrapy.Field()
    char_num = scrapy.Field()
    last_update = scrapy.Field()

    # 总点击数，本月点击，本周点击
    total_click_num = scrapy.Field()
    month_click_num = scrapy.Field()
    week_click_num = scrapy.Field()

    # 总推荐数，本月推荐，本周推荐
    total_recommend = scrapy.Field()
    month_recommend = scrapy.Field()
    week_recommend = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
将数据保存到MongoDB
'''

import pymongo

class DingdianPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_port,mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_port = mongo_port
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_HOST'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_port = crawler.settings.get('MONGODB_PORT'),
            mongo_collection = crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert_one(dict(item))
        return item

'''
# 存储items到JSON文件
import json

class DingdianPipeline(object):

    def open_spider(self,spider):
         self.file = open('./items.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
'''

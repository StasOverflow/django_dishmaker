# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy_aizel_scrapper.settings import ITEM_BULK_SIZE
from scrapy_aizel import tasks


class ScrapyParsePipeline(object):

    def __init__(self):
        super(ScrapyParsePipeline, self).__init__()
        self.items = list()

    def process_item(self, item, spider):
        # print(spider)
        self.items.append(dict(item))  # since object of type'AizelClothItem' is not json serializable
        if len(self.items) >= ITEM_BULK_SIZE:
            self.handle_list_of_items()
        return item

    def handle_list_of_items(self):
        if len(self.items):
            print('now i have to save some items ', len(self.items))
            tasks.items_transfer.delay(self.items)
            self.items = list()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """
        If present, this classmethod is called to create a pipeline
        instance from a Crawler. It must return a new instance of the pipeline.

        Note: redis spider can't be closed, it has idle state
        """
        pipeline = cls()
        crawler.signals.connect(pipeline.handle_list_of_items, signal=signals.spider_idle)
        return pipeline

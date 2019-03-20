# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class ScrapyParsePipeline(object):

    def __init__(self):
        super(ScrapyParsePipeline, self).__init__()
        # dispatcher.connect(self.spider_opened, signals.spider_opened)
        # dispatcher.connect(self.closed, signals.spider_closed)
        self.items = list()

    def process_item(self, item, spider):
        # print(spider)
        self.items.append(item)
        if len(self.items) >= 5:
            self.handle_list_of_items()
        return item

    def handle_list_of_items(self):
        print('now i have to save some items ', len(self.items))
        self.items = list()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """
        If present, this classmethod is called to create a pipeline
        instance from a Crawler. It must return a new instance of the pipeline.

        """
        pipeline = cls()
        crawler.signals.connect(pipeline.closed, signal=signals.spider_opened)
        crawler.signals.connect(pipeline.closed, signal=signals.spider_closed)
        return pipeline

    def closed(self):
        print("''''''''''gdfgmdfpkgmdfvmdfpam[vdfpmv[dpfzmvfpsbmfbdf\n\n\n\n\n\n\gfcsdgfdgfdgfdgdfgdfgdfgdfg''''''")
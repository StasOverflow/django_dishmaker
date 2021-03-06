import scrapy
from scrapy_aizel_scrapper.items import AizelClothItem
from scrapy_redis.spiders import RedisSpider
from scrapy_aizel_scrapper.settings import SPIDER_QUICK_MODE


# start_urls = ("https://aizel.ru/ua-ru/odezhda/bryuki/", )

class AizelClothSpider(RedisSpider):
    name = "aizel"

    def __init__(self):
        super().__init__()
        self.item_count = 0

    size_base_url = 'https://aizel.ru/products/sizes/?id='

    def field_format(self):
        pass

    def parse(self, response):
        link = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        last_page = response.xpath('//ul[@class="pagination"]/li[last()]/a/text()').get()
        url_list = [
            response.urljoin(link[:-2] + str(x+1)) for x in range(int(last_page))
        ]
        if SPIDER_QUICK_MODE:
            url_list = url_list[4:7]
        for index, link in enumerate(url_list):
            yield scrapy.Request(url_list[index], self.parse_cloth_list)

    def parse_cloth_list(self, response):
        cloth_link_list = response.xpath('//ul[contains(@class, "product__list")]/'
                                         'li[contains(@class, "product__item")]//'
                                         'a[contains(@class, "product__desc__name")]/'
                                         '@href').getall()

        if SPIDER_QUICK_MODE:
            cloth_link_list = cloth_link_list[1:5]
        for index, link in enumerate(cloth_link_list):
            item_id = link.split('-')[-1].strip('/')
            yield scrapy.Request(response.urljoin(link), self.parse_cloth_fields, meta={'item_id': item_id})

    def parse_cloth_fields(self, response):
        meta_dict = dict()
        meta_dict['brand'] = response.xpath('//h1[@itemprop="name"]/a/text()').get()
        meta_dict['title'] = response.xpath('//h1[@itemprop="name"]/span/text()').get()
        meta_dict['image'] = response.xpath('//img[@itemprop="image"]/@src').get()
        meta_dict['price'] = response.xpath('//span[contains(@itemprop, "price")]/text()').get()
        meta_dict['descr'] = response.xpath('//p[contains(@itemprop, "description")]/text()').get()
        meta_dict['color'] = response.xpath('//div[@class="details__row"]/'
                                            'span[contains(text(), "Цвет")]/../text()').get()

        size_request_url = self.size_base_url + response.meta['item_id'] + '/'
        return scrapy.Request(size_request_url, self.parse_cloth_item_with_size, meta=meta_dict)

    def price_get(self, response):
        price_string = ''
        price_string_list = response.meta['price'].rstrip(' ').split(' ')
        for digit in price_string_list:
            price_string += digit
        return int(price_string)

    def image_get(self, response):
        return response.urljoin(response.meta['image'])

    def sizes_get(self, response):
        return response.xpath('//ul[contains(@class, "size__list")]//'
                              'span[@class="product-size-title"]/text()').getall()

    def color_get(self, response):
        return response.meta['color'].rstrip(' ').split(' ')[-1]

    def parse_cloth_item_with_size(self, response):
        fields_item = AizelClothItem()
        fields_item['brand'] = response.meta['brand']
        fields_item['title'] = response.meta['title']
        fields_item['image'] = self.image_get(response)
        fields_item['price'] = self.price_get(response)
        fields_item['sizes'] = self.sizes_get(response)
        fields_item['descr'] = response.meta['descr']
        fields_item['color'] = self.color_get(response)
        self.item_count += 1
        return fields_item

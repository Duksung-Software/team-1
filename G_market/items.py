import scrapy


class GMarketItem(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    Delivery_charge = scrapy.Field()
    URL = scrapy.Field()

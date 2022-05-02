import scrapy

class GMarketItem(scrapy.Item):
    
    Name = scrapy.Field()

    Price = scrapy.Field()

    Delivery_Charge = scrapy.Field()

    URL = scrapy.Field()

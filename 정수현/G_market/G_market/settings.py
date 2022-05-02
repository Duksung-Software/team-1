BOT_NAME = 'G_market'

SPIDER_MODULES = ['G_market.spiders']
NEWSPIDER_MODULE = 'G_market.spiders'

ROBOTSTXT_OBEY = False

LOG_FILE = 'G_Maket.log'
FEED_EXPORT_ENCODING="utf-8-sig"
FEED_EXPORT_FIELDS = ['Name', 'Price', 'Delivery_Charge', 'URL']
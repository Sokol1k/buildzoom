from scrapy.item import Item, Field

class UrlsItem(Item):
    url = Field()
    status = Field()
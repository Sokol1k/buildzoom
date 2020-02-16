import scrapy
from scrapy.utils.sitemap import Sitemap
from scrapy.spiders.sitemap import SitemapSpider
from items.UrlsItem import UrlsItem


class SiteMapSpider(SitemapSpider):
    name = 'sitemap'
    host = 'https://www.buildzoom.com'
    # sitemap_urls = ['https://www.buildzoom.com/sitemap.xml']

    def start_requests(self):
        yield scrapy.Request(url=f'{self.host}/sitemap.xml', callback=self.parse, meta={'proxy': 'http://192.168.11.82:9966'})

    def parse(self, response):
        response = Sitemap(response.body)
        count = 0
        for url in response:
            if url['loc'].find('contractors') + 1:
                count = count + 1
                yield scrapy.Request(url=url['loc'], callback=self.parse_contractors)
            if count == 1:
                break

    def parse_contractors(self, response):
        response = Sitemap(response.body)
        for url in response:
            if url['loc'] == self.host:
                continue
            yield UrlsItem(**{
                'url': url['loc'],
                'status': 0
            })


# scrapy.utils.sitemap.Sitemap
# scrapy.http.response.xml.XmlResponse
# scrapy crawl sitemap --output=data.json -L WARNING

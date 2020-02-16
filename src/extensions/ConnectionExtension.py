import scrapy
import pika
from scrapy import signals
from spiders.ContractorSpider import ContractorSpider


class ConnectionExtension(object):

    def __init__(self):
        url = 'amqp://dexgjlns:i4SAIT92KeuaM1ezoU4LjOkLGsdO8e7x@stingray.rmq.cloudamqp.com/dexgjlns'
        params = pika.URLParameters(url)
        connection = pika.SelectConnection(params, on_open_callback=self.on_connected)
        try:
            connection.ioloop.start()
        except KeyboardInterrupt:
            connection.ioloop.stop()
            connection.close()
    
    def on_connected(self, connection):
        connection.channel(on_open_callback=self.on_channel_open)
    
    def on_channel_open(self, new_channel):
        self.channel = new_channel
        self.channel.queue_declare(queue='urls', durable=True, callback=self.on_queue_declared)

    def on_queue_declared(self, frame):
        self.channel.basic_consume('urls', self.callback)

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        ConnectionExtension.crawler = crawler
        return ext

    def callback(self, ch, method, properties, body):
        spider = self.crawler.spider
        self.crawler.engine.crawl(scrapy.Request(
            url=str(body.url), callback=spider.parse), spider)
        self.channel.basic_ack(method.delivery_tag)

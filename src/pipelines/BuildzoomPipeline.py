import pika
from database.Connection import Connection
from items.UrlsItem import UrlsItem
from items.ContractorItem import ContractorItem


class BuildzoomPipeline(object):
    def __init__(self):
        self.connect = Connection()

    def process_item(self, item, spider):
        if isinstance(item, UrlsItem):
            self.connect.setUrl(item)
        if isinstance(item, ContractorItem):
            url = 'amqp://dexgjlns:i4SAIT92KeuaM1ezoU4LjOkLGsdO8e7x@stingray.rmq.cloudamqp.com/dexgjlns'
            params = pika.URLParameters(url)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            channel.queue_declare(queue='items')
            channel.basic_publish(
                exchange='', routing_key='items', body=item)
            connection.close()

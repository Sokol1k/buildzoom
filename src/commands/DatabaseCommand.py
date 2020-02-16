import pika
import time
from database.Connection import Connection
from scrapy.commands import ScrapyCommand


class DatabaseCommand(ScrapyCommand):
    def __init__(self, *a, **kw):
        self.db = Connection()

    def run(self, args, opts):
        try:
            url = 'amqp://dexgjlns:i4SAIT92KeuaM1ezoU4LjOkLGsdO8e7x@stingray.rmq.cloudamqp.com/dexgjlns'
            params = pika.URLParameters(url)
            connection = pika.BlockingConnection(params)
            self.channel = connection.channel()
            self.channel.queue_declare(queue='items')
            self.channel.basic_consume('items', self.callback)
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()

    def callback(self, ch, method, properties, body):
        self.db.changeUrlStatus(body.id, 2)
        self.db.setContractor(body)
        self.channel.basic_ack(method.delivery_tag)


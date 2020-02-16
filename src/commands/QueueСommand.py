import pika
import time
from database.Connection import Connection
from scrapy.commands import ScrapyCommand


class QueueСommand(ScrapyCommand):
    def __init__(self, *a, **kw):
        self.db = Connection()

    def run(self, args, opts):
        url = 'amqp://dexgjlns:i4SAIT92KeuaM1ezoU4LjOkLGsdO8e7x@stingray.rmq.cloudamqp.com/dexgjlns'
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        MAX_QUEUE_LENGTH = 10
        while True:
            try:
                queue_count = channel.queue_declare(queue='urls')
                if int(queue_count.method.message_count) < MAX_QUEUE_LENGTH:
                    url = self.db.getUrl()
                    channel.basic_publish(
                        exchange='', routing_key='urls', body=url)
                    self.db.changeUrlStatus(url.id, 1)
                else:
                    time.sleep(1)
            except KeyboardInterrupt:
                break
        connection.close()

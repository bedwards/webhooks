from time import sleep
import boto3
from django.core.management.base import BaseCommand
import requests
from app.models import Webhook


client = boto3.resource('sqs',
                        endpoint_url='http://mq:9324',
                        region_name='elasticmq',
                        aws_secret_access_key='x',
                        aws_access_key_id='x',
                        use_ssl=False)

queue = client.get_queue_by_name(QueueName='events')


class Command(BaseCommand):
    help = 'Grab messages off event queue, find webhook configs, send webhooks'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        while True:
            configs = Webhook.objects.all()
            messages = queue.receive_messages(MaxNumberOfMessages=10)

            if not messages:
                sleep(1)
                continue

            delete_resp = queue.delete_messages(
                Entries=[
                    {
                        'Id': str(i),
                        'ReceiptHandle': m.receipt_handle
                    }
                    for i, m in enumerate(messages)
                ])
            self.stdout.write(self.style.SUCCESS('Deleted %r' % delete_resp))

            for msg in messages:
                for config in configs:
                    try:
                        requests.post(config.url, data=msg.body)
                    except requests.exceptions.RequestException:
                        pass

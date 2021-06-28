import sys
import boto3

client = boto3.resource('sqs',
                        endpoint_url='http://localhost:9324',
                        region_name='elasticmq',
                        aws_secret_access_key='x',
                        aws_access_key_id='x',
                        use_ssl=False)

queue = client.get_queue_by_name(QueueName='events')


event = "Hello webhooks world"
if len(sys.argv) > 1:
    event = ' '.join(sys.argv[1:])
queue.send_message(MessageBody='{"event": "%s"}' % event)

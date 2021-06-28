import boto3

sqs_endpoint = 'localhost'
sqs_port = '9324'

client = boto3.resource('sqs',
                        endpoint_url='http://localhost:9324',
                        region_name='elasticmq',
                        aws_secret_access_key='x',
                        aws_access_key_id='x',
                        use_ssl=False)

queue = client.get_queue_by_name(QueueName='events')
queue.send_message(MessageBody='{"foo": "bar"}')

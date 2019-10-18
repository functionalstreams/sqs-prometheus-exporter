import logging
import os
import time
import boto3
from prometheus_client import start_http_server
from prometheus_client import Gauge

os.environ['QUEUES_TO_MONITOR'] = "mparticle"
log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
queues_to_monitor = os.environ['QUEUES_TO_MONITOR'].split(",")
region = os.environ['AWS_REGION']

logging.basicConfig(level=log_level)


approximate_number_of_messages = Gauge('approximate_number_of_messages', 'Number of messages available', ['queue'])
approximate_number_of_messages_delayed = Gauge('approximate_number_of_messages_delayed', 'Number of messages delayed',
                                               ['queue'])
approximate_number_of_messages_not_visible = Gauge('approximate_number_of_messages_not_visible',
                                                   'Number of messages in flight', ['queue'])

sqs = boto3.resource('sqs', region_name=region)


def update_metrics():
    """
    Updates the values of the prometheus metrics with the values of the attributes from each SQS queue
    """
    for queue_name in queues_to_monitor:
        q = sqs.get_queue_by_name(QueueName=queue_name)
        logging.debug(f"Updating metrics for queue [{queue_name}]")

        approximate_number_of_messages.labels(queue=queue_name).set(
            q.attributes.get('ApproximateNumberOfMessages'))
        approximate_number_of_messages_not_visible.labels(queue=queue_name).set(
            q.attributes.get('ApproximateNumberOfMessagesNotVisible'))
        approximate_number_of_messages_delayed.labels(queue=queue_name).set(
            q.attributes.get('ApproximateNumberOfMessagesDelayed'))


if __name__ == '__main__':

    start_http_server(9095)
    logging.info("Started metrics exporter at port 9095")

    while True:
        update_metrics()
        time.sleep(10)

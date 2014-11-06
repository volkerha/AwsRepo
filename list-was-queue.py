# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

conn.create_queue("d14123127")
rs = conn.get_all_queues()
print("Region Ireland:")
for q in rs:
	print q.id
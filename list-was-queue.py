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

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

conn2 = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

rs = conn.get_all_queues()
rs2 = conn.get_all_queues()
print("Region Us-East:\n")
for q in rs:
	print q.id
print("Region Ireland:\n")
for q in rs2:
  print q.id
import logging.handlers
from datetime import datetime

import os
import boto3
import json
from flask import request


logger = logging.getLogger(__name__)
level = logging.getLevelName('INFO')
logger.setLevel(level)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

sout_handler = logging.StreamHandler()
sout_handler.setLevel(level)
sout_handler.setFormatter(formatter)
logger.addHandler(sout_handler)


dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id=os.environ.get('aws_access_key'),
                          aws_secret_access_key=os.environ.get('aws_secret_access_key'))


def generate_epoch():
    return int(datetime.now().replace(microsecond=0, second=0).strftime('%s'))


def put_conversation_item(message, chat_id):
    try:

        table = dynamodb.Table('Conversations')

        logger.info(f'Adding detail for chatID, {chat_id}: {message}')

        message_item = {
                'conversation_id': chat_id,
                'message_sent_on': generate_epoch(),
                'message': message
            }

        response = table.put_item(Item=message_item)
        status_code = response['ResponseMetadata'].get('HTTPStatusCode')
        logger.info(f'Dynamo Response Code: {status_code}')

        if status_code != 200:
            raise IOError('Unable to put item into DynamoDB')

        return message_item
    except Exception as e:
        logger.exception(e)
        raise e


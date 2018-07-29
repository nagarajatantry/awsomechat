import logging.handlers
from datetime import datetime

import boto3
import json
from flask import request


LOGFILE = 'api_service.log'
logger = logging.getLogger(__name__)
level = logging.getLevelName('INFO')
logger.setLevel(level)
handler = logging.handlers.RotatingFileHandler(LOGFILE, maxBytes=5 * 1024 * 1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

sout_handler = logging.StreamHandler()
sout_handler.setLevel(level)
sout_handler.setFormatter(formatter)
logger.addHandler(sout_handler)


def generate_epoch():
    return int(datetime.now().replace(microsecond=0, second=0).strftime('%s'))


def put_conversation_item(message, chat_id):
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id="AKIAJTWULVH2GINWFOFA", aws_secret_access_key="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")

        table = dynamodb.Table('Conversations')

        logger.info(f'Adding detail for chatID, {chat_id}:', message)

        message_item = {
                'conversation_id': chat_id,
                'message_sent_on': generate_epoch(),
                'message': message
            }

        h = table.put_item(Item=message_item)
        print(h)
        return message_item
    except Exception as e:
        logger.exception(e)
        raise e

import logging.handlers

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

from api_service import put_conversation_item

LOGFILE = 'engine.log'
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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C>\xd1K\xb1zh]\xa4<I+\xf4\x14qm9m\xcd\xd5\xd1\xca\xb7\x95'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


@app.route('/hello', endpoint='hello', methods=['GET'])
def hello():
    try:
        name = 'Friend'
        logger.info(f'Response: "Hello, {name}! I am working"')
        return jsonify({'result': f"Hello, {name}! I am working!"}), 200
    finally:
        logger.info(f'Executed /hello - {name}')


@app.route('/getmessage', endpoint='get_message', methods=['GET'])
def get_message():
    pass


@app.route('/sendmessage', endpoint='send_message', methods=['PUT'])
def send_message():
    try:
        message = request.get_json()
        chat_id = message.get('chat_id')
        new_message = message.get('data')

        message_item = put_conversation_item(new_message, chat_id)

        return jsonify({'data': message_item})
    except Exception as e:
        logger.exception(e)
        return jsonify({'data': f'Error: {e}'})


if __name__ == '__main__':
    logger.info('Starting App...')
    app.run(host='0.0.0.0', port=5000)





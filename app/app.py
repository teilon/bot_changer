from flask import Flask
from flask import request
from flask import jsonify
import requests
import re

from flask_sslify import SSLify
# from config import tengiz_token

app = Flask(__name__)
sslify = SSLify(app)


# def query(method):
#     return 'https://api.telegram.org/bot{token}/{method}'.format(
#         token=tengiz_token,
#         method=method
#     )


# def set_message(chat_id, text='hello', reply_to_message_id=-1):
#     url = query('sendMessage')
#     answer = {'chat_id': chat_id,
#               'text': text}
#     if reply_to_message_id != -1:
#         answer['reply_to_message_id'] = reply_to_message_id
#     r = requests.post(url, json=answer)
#     return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    # if request.method == 'POST':
    #     r = request.get_json()
    #     message_json = r['message']
    #     chat_id = message_json['chat']['id']
    #     message = message_json['text']
    #     reply_to_message_id = int(message_json['message_id'])
    #     print('\nZ\n'.format(type(reply_to_message_id)))
    #     print('\nY\n'.format(message))
    #
    #     return jsonify(r)
    return '<h1>Bot welcomes you</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='127.0.0.1', port=5000)
    # app.run()

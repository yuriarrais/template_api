from flask import Flask, jsonify, request
from flask_cors import CORS
# from helpers.session_helper import *
# from helpers.constants import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['JSON_SORT_KEYS'] = False


CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return '<p> Hello New World Flask!!!</p>'


from src.app.controllers.user import *

if __name__ == '__main__':
    app.run(debug=True, host='localhost')

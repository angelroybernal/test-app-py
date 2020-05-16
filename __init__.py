import os
from flask import Flask, jsonify
app = Flask(__name__)

_port = os.environ.get('PORT', 5000)
_username = os.environ.get('MYAPP_USERNAME', 'World')

@app.route('/')
def hello():
    return jsonify('Hello %s!' % _username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_port, debug=True)

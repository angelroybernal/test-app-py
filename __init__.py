import os
from flask import Flask
app = Flask(__name__)

_port = os.environ.get('PORT', 5000)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_port)
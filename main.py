from slack_api import connect
from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def start():
    connect()
    return "app running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)

#!/Users/andrzejmazur/virtualenvironment/simple_web_server_app/bin/python

from flask import Flask
import time
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    ts = time.time()
    current_time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return "[" + current_time + "] GET Request Received by simple_web_server_app.py"

if __name__ == "__main__":
    app.run()

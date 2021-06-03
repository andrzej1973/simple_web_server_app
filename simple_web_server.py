#!/usr/bin/python3

from flask import Flask
import time
import datetime

application = Flask(__name__)


@application.route("/")
def hello():
    ts = time.time()
    current_time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return "[" + current_time + "] GET Request Received by simple_web_server.py"

if __name__ == "__main__":
    application.run()

#!/usr/local/bin/python3

from flask import Flask
import os
import time
import datetime

application = Flask(__name__)


@application.route("/")
def hello():
	ts = time.time()
	current_time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	this_script_name = os.path.basename(__file__)
	command = "hostname"
	res = os.popen(command)
	container_id = res.read()
	return "[" + current_time + "] HTTP GET request received by " + this_script_name + " script running inside the container with id: " + container_id + "\n"
if __name__ == "__main__":
	application.run(host="0.0.0.0", port="5001", debug=True)


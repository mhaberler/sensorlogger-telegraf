
# logs sensorlogger input to log.js
# run as:
# flask run --host=0.0.0.0 --port=<portnumber>

# in sensorlogger, configure HTTP push as:
# http://<thisip>:<portnumber>/sensorlogger

from datetime import datetime
import json

from flask import Flask, request

app = Flask(__name__)

fd = open("log.js", "w")



@app.route("/sensorlogger", methods=["POST"])
def data():  # listens to the data streamed from the sensor logger
    if str(request.method) == "POST":
        print(f'received data: {request.data}')
        data = json.loads(request.data)
        fd.write(json.dumps(data, indent=4))
        fd.write("\n\n")
    return "success"


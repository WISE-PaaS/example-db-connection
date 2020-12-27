import ex_mongodb.connect
import ex_influxdb.connect

from flask import Flask
app = Flask(__name__)

@app.route("/")
def ping():
    return "app is up!"

@app.route("/testmongo")
def connectMongo():
    return ex_mongodb.connect.testMongo()

@app.route("/testinflux")
def connectInflux():
    return ex_influxdb.connect.testInflux()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
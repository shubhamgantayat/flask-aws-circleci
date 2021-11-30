from flask import Flask
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
import os

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "App is running.hello world.jkhhhhjj"


if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.getenv("PORT", 5000))
    app.run(host=host, port=port, debug=True)

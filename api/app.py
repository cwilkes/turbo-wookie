from flask import Flask, request, jsonify
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/users', methods=['POST', ])
def users_create():
    user_name = request.form['name']
    return jsonify({'yo': user_name})



if __name__ == "__main__":
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT)

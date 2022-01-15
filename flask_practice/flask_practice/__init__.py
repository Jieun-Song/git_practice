from flask import Flask

app = Flask(__name__)


@app.route("/")
def flask_practice():
    return "Hello world"
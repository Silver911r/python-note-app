from flask import Flask, request
from flask_pymongo import PyMongo

import config

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://silver911r:{config.mongo_pass}@cluster0.ggyrd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
def home():
    return "<p>The home page</p>"


if __name__ == "__main__":
    app.run(debug=True)

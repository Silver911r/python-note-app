from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo

import config

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://{config.username}:{config.mongo_pass}@cluster0.ggyrd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
def home():
    return "<p>The home page</p>"


@app.route('/add-note', methods=['GET', 'POST'])
def addNote():
    if(request.method == "GET"):
        return "<p>Add note page</p>"
    elif(request.method == "POST"):
        # logic for adding a note
        pass


@app.route('/edit-note', methods=["GET", "POST"])
def editNote():
    if(request.method == "GET"):
        return "<p>Edit note page</p>"
    elif(request.method == "POST"):
        # logic for editing a note
        pass


@app.route('/delete-note', methods=["POST"])
def deleteNote():
    # logic here
    pass


if __name__ == "__main__":
    app.run(debug=True)

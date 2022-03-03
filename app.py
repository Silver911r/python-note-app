from pydoc import describe
from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo, ObjectId
import datetime

import config


app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://{config.username}:{config.mongo_pass}@cluster0.ggyrd.mongodb.net/db?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
def home():

    # get notes form teh database
    notes = list(mongo.db.notes.find({}).sort("createdAt", -1))

    # render a view
    return render_template("/pages/home.html", homeIsActive=True, addNoteIsActive=False, notes=notes)


@app.route('/add-note', methods=['GET', 'POST'])
def addNote():
    if(request.method == "GET"):
        return render_template("pages/add-note.html", homeIsActive=False, addNoteIsActive=True)
    elif(request.method == "POST"):

        # get the fields data
        title = request.form['title']
        description = request.form['description']
        createdAt = datetime.datetime.now()

        # save teh records to the database
        mongo.db.notes
        mongo.db.notes.insert_one(
            {"title": title, "description": description, "createdAt": createdAt})

        # redirect to home page
        return redirect("/")


@app.route('/edit-note', methods=["GET", "POST"])
def editNote():
    if(request.method == "GET"):
        # get the id of the note to edit
        noteId = request.args.get('form')

        # get teh note details from the db
        note = dict(mongo.db.notes.find_one({"_id": ObjectId(noteId)}))

        # direct to edit note page
        return render_template('pages/edit-note.html', note=note)
    elif(request.method == "POST"):

        # get the data of the note
        noteId = request.form['_id']
        title = request.form['title']
        description = request.form['description']

        # update the data in the db
        mongo.db.notes.update_one({"_id": ObjectId(noteId)}, {
                                  "$set": {"title": title, "description": description}})

        # redirect to home page
        return redirect("/")


@app.route('/delete-note', methods=["POST"])
def deleteNote():

    # get the id of the note to delete
    noteId = request.form['_id']

    # delete from the database
    mongo.db.notes.delete_one({"_id": ObjectId(noteId)})

    # redirect to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

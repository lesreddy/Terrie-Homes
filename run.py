import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Terrie_Homes'
app.config["MONGO_URI"] = 'mongodb+srv://Redler:LakeBoga29@myfirstcluster-rvlcz.mongodb.net/Terrie_Homes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/listings")
def listings():
    return render_template("listings.html", for_sale=mongo.db.for_sale.find())

if __name__== "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
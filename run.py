import env
import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Terrie_Homes'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "No ENV Value")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html")
    return render_template("dashboard.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/login", methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if (bcrypt.checkpw(request.form['pass'].encode('utf-8'), login_user['password'])):
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('signin'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/listings")
def listings():
    return render_template("listings.html", for_sale=mongo.db.for_sale.find())

if __name__== "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
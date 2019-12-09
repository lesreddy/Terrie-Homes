import env
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import bcrypt

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
        return render_template("dashboard.html",for_sale=mongo.db.for_sale.find())
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
        return flash ("Unfortunately that is an invalid username or password! Please Try Again")
    return render_template("signin.html")

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
        
        flash ("Username already used!")
            
    return render_template('register.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash ("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html")

@app.route("/listings")
def listings():
    return render_template("listings.html", for_sale=mongo.db.for_sale.find())    

@app.route("/insert_listings", methods=['POST'])
def insert_listings():
    listings = mongo.db.for_sale
    listings.insert_one(request.form.to_dict())
    return redirect(url_for('dashboard'))

@app.route("/edit_listing/<listing_id>")
def edit_listing(listing_id):
    the_listing = mongo.db.for_sale.find_one({"_id": ObjectId(listing_id)})
    return render_template("editlisting.html", listing=the_listing, for_sale=mongo.db.for_sale.find())

@app.route("/update_listing/<listing_id>", methods=["POST"])
def update_listing(listing_id):
    listing = mongo.db.for_sale
    listing.update( {'_id': ObjectId(listing_id)},
    {
        'address':request.form.get('address'),
        'bedrooms':request.form.get('bedrooms'),
        'bathrooms': request.form.get('bathrooms'),
        'property_type': request.form.get('property_type'),
        'price':request.form.get('price')
    })
    return redirect(url_for('dashboard'))

@app.route('/delete_listing/<listing_id>')
def delete_listing(listing_id):
    mongo.db.for_sale.remove({'_id': ObjectId(listing_id)})
    return redirect(url_for('dashboard'))

if __name__== "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
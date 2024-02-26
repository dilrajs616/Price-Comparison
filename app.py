from flask import Flask, render_template, session, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from functools import wraps
import os
import time

app = Flask(__name__)
URI = os.getenv("MONGO_URI")

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['MONGO_URI'] = URI

# Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi('1'))
db = client.UserData

from product import routes
from user import routes

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)      
        else:
            return redirect('/')  
    return wrap


@app.route("/")
def landing():
    if "logged_in" not in session:
        return render_template("landing.html")
    else:
        return redirect("/dashboard")

@app.route("/authentication")
def authentication():
    return render_template("authentication.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", session = session["user"])


if __name__ == "__main__":
    app.run(debug=True)
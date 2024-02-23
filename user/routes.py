from flask import redirect, jsonify
from app import app
from user.models import User

@app.route("/user/signup", methods=["POST"])
def signup():
    response, code = User().signup()
    if code == 200:
        return redirect("/dashboard")
    else:
        return response

@app.route("/user/login", methods=["POST"])
def login():
    response, code = User().login()
    if code == 200:
        return redirect("/dashboard")
    else:
        return response

@app.route("/user/logout", methods=["POST"])
def logout():
    if User().logout():
        return redirect("/")
    
    else:
        return redirect("/dashboard")
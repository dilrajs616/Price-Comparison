from flask import redirect, flash
from app import app
from user.models import User

@app.route("/user/signup", methods=["POST"])
def signup():
    response, code = User().signup()
    if code == 200:
        flash("signup successful", "info")
        return redirect("/dashboard")

    flash(response["error"], "error")
    return redirect("/authentication")

@app.route("/user/login", methods=["POST"])
def login():
    response, code = User().login()
    if code == 200:
        flash("login successful", "info")
        return redirect("/dashboard")

    flash(response["error"], "error")
    return redirect("/authentication")

@app.route("/user/logout", methods=["POST"])
def logout():
    if User().logout():
        return redirect("/")
    
    else:
        flash("failed to logout", "info")
        return redirect("/dashboard")
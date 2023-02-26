# from flasktest6.py
# import sqlalchemy to use database
from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)

# all session data is encrypted on the server
# so we need to define a "secret key" which will be how we encrypt and decrypt the data
app.secret_key = "chickennuggets"
# to set how long the session can last
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
def home():
    return render_template("child.html")

# methods we can use on login page
@app.route("/login", methods=["POST", "GET"])
def login():
    # if we get a "POST" request, get the info from the input box
    if request.method == "POST":
        # makes session permanent
        session.permanent = True
        # stores our user's name
        # put dictionary key "nm" that we wanna access for the name corresponding for whatever input we had
        # gives us the data typed in the input box
        user = request.form["nm"]
        # sets up data for a session, stores data as a dictionary (key and value)
        session["user"] = user
        # to flash login successful
        flash("Login Successful!", "info")
        return redirect(url_for("user"))
    # if we get a "GET" request, render the login template (submit button not clicked)
    else:
        # check if user is already logged in
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    # get session information
    # check if there is any information in session
    if "user" in session:
        user = session["user"]

        # if request method is POST, grab email from the email field
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email = email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

# to logout of session and delete session information
@app.route("/logout")
def logout():
    # check if user was logged in first
    if "user" in session:
        user = session["user"]
        # flashes this message after logout (code has to be added into login.html to display flash messages)
        flash(f"You have been logged out, {user}", "info")
        # removes user data from dictionary
        session.pop("user", None)
        session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
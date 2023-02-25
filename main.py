# main file

from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/selection", methods = ["POST", "GET"])
def selection():
    return render_template("selection.html")

if __name__ == "__main__":
    app.run(debug=True)
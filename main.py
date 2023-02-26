# main file

import summariser

from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_session import Session
import requests
from pdfminer.high_level import extract_text
# from werkzeug import secure_filename
# import os, os.path
from distutils.log import debug
from fileinput import filename
from datetime import timedelta

# make GET request to the API endpoint
response = requests.get("https://www.dictionaryapi.com/api/v3/references/medical/json/%7Bdoctor%7D?key=812c2608-27b6-46a5-b51a-7a14af262155")
# prints error 404, or 200 (all good) etc
print(response.status_code)
d = response.json()
for result in d:
    print(result["meta"]["stems"])
    print(result["fl"])
    for shortdef in result["shortdef"]:
        print(shortdef)
print(type(d[0]))


app = Flask(__name__)
# uses server-side instead of client-side so there is no limit
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)
app.secret_key = "chickennuggets"
app.permanent_session_lifetime = timedelta(minutes = 5)

# homepage
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        print("here!")
        session.clear()
        f = request.files["file"]
        f.save(f.filename)
        text = extract_text(f.filename)
        summary = summariser.summarize(text)
        session["text"] = text
        session["filename"] = f.filename
        session["summary"] = summary
        flash("Upload Successful!", "info")
        return redirect(url_for("selection"))
    else:
        if "filename" in session:
            filename = session["filename"]
            flash(f"{filename} has already been uploaded!")
        return render_template("home.html")

# presentation style selection page
@app.route("/selection", methods = ["POST", "GET"])
def selection():
    if "filename" in session:
        return render_template("selection.html", name = session["filename"], summary=session["summary"])
    else:
        flash("No file in session!", "info")
        return redirect(url_for("home"))
        
# page for definitions
# @app.route("/definitions")
# def definitions():


if __name__ == "__main__":
    app.run(debug=True)
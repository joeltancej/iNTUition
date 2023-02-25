# main file

from flask import Flask, render_template, url_for, request, redirect, session, flash
from pdfminer.high_level import extract_text
from distutils.log import debug
from fileinput import filename
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "chickennuggets"
app.permanent_session_lifetime = timedelta(minutes = 5)

# homepage
@app.route("/")
def home():
    # if "filename" in session:
    #     flash("File already uploaded, would you like to continue?", "info")
    return render_template("home.html")

# presentation style selection page
@app.route("/selection", methods = ["POST", "GET"])
def selection():
    if request.method == 'POST': 
        # session.permanent = True
        f = request.files["file"]
        f.save(f.filename)
        # text = extract_text(f)
        # session["filename"] = f.filename
        return render_template("selection.html", name = f.filename)
    else:
        if "filename" in session:
            return render_template("selection.html", name = session["filename"])
        else:
            return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
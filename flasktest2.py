from flask import Flask, redirect, url_for, render_template

#create instance of the flask web app
app = Flask(__name__)

#homepage
#renders html template
#passes value into the function as a parameter, and pass the variables into the HTML template
@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name, r = 2, content_1 = ["Tim", "Joe", "Bill"])

if __name__ == "__main__":
    app.run()
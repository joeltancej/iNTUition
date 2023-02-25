from flask import Flask, redirect, url_for

#create instance of the flask web app
app = Flask(__name__)

#homepage
@app.route("/")
def home():
    #return inline html
    return "BABY! This is the main page <h1>BABY<h1>"

#passing value to function as a parameter
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

#administrator page, should only be accessible to admin
#redirect user to user page, passing "Admin" in as a parameter.
@app.route("/admin")
def admin():
    return redirect(url_for("user", name = "Admin"))

if __name__ == "__main__":
    app.run()
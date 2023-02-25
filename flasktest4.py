# HTTP methods - GET and POST
# GET - gets or sends info to a website or client
# POST - does the above securely

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("child.html")

# methods we can use on login page
@app.route("/login", methods=["POST", "GET"])
def login():
    # if we get a "POST" request, get the info from the input box
    if request.method == "POST":
        # stores our user's name
        # put dictionary key "nm" that we wanna access for the name corresponding for whatever input we had
        # gives us the data typed in the input box
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    # if we get a "GET" request, render the login template (submit button not clicked)
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
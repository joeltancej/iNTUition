#template inheritance - useful too so html code or javascript code etc.
#helps to create a "base" template
#using bootstrap to make decent frontend frameworks without having to use some frameworks like React

from flask import Flask, redirect, url_for, render_template

#create instance of the flask web app
app = Flask(__name__)

#homepage
#renders html template
#passes value into the function as a parameter, and pass the variables into the HTML template
@app.route("/")
def home():
    return render_template("child.html")

if __name__ == "__main__":
    #debug=True allows us to not have to re-run the server every time we make a change.
    #it will automatically detect the changes and update the website for us
    app.run(debug=True)
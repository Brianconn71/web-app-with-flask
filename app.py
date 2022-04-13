from flask import Flask, render_template, request, flash

# creates class from app
app = Flask(__name__)
app.secret_key = "hooray"

@app.route("/home")
def index():
    flash("What is your name?")
    return render_template("index.html")


@app.route("/greeting", methods=["POST", "GET"])
def greeting():
    flash("Hi " + str(request.form['name']) + ', how are ya keeping?')
    return render_template("templates/index.html")

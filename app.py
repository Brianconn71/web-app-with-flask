from flask import Flask, render_template, request, flash

# creates class from app
app = Flask(__name__)

@app.route("/home")
def index():
    flash("What is your name?")
    return render_template("../index.html")
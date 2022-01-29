from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)

app.secret_key = 'supersecretkey'

@app.route('/generator')
def index():
    flash("Insert length of password")
    return render_template("index.html")

@app.route("/var1", methods=["POST","GET"])
def var1():
    pass_len = request.form['name_input']
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s, int(pass_len)))
    flash("Insert length of password")
    flash(p)
    return render_template("index.html")



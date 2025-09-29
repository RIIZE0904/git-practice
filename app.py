from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('menu.html')

@app.route("/test1")
def test1():
    return render_template('test1.html')
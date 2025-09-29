from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('menu.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')
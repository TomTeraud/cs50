from flask import Flask, render_template, redirect

app = Flask(__name__)

KATALOGS = {}

FRUITS = [
    "apple",
    "bannana",
    "orange",
    "watermelon"
]

@app.route('/')
def index():
    return render_template("index.html", augli = FRUITS)
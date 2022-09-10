from flask import Flask, render_template, redirect, request

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

@app.route("/parbaude", methods=['POST'])
def ievade():
    vards = request.form.get('vards')
    
    auglis = request.form.get('auglis')
    KATALOGS[vards] = auglis


    return redirect("/db")

@app.route("/db")
def izeja():
    return render_template("izeja.html", iz = KATALOGS)

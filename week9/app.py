from crypt import methods
from re import X
from unicodedata import name
from flask import Flask, render_template, request 

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sveicinats", methods=['POST'])
def atbilde():
    x = request.args.get("q", "janis") # input janis if empty form
    y = request.args.get("qq", "jansons") # --``--
    z = request.form.get("p","password")
    return render_template("sveiciens.html", pirmais = x, otrais = y, parole = z)


#if __name__=='__main__':
app.run()

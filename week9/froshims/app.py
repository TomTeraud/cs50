from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reg..", methods=["POST"])
def reg():

    # validate submission
    if not request.form.get("x") or request.form.get("y") not in ["A", "B", "C"]:
        return render_template("failure.html")
    
    # Confirm registration
    return render_template("success.html")

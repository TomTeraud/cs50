from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGZ = {}

CARS = [
    "Audi",
    "Ford",
    "Bmw",
    "Tesla"
]

@app.route('/')
def index ():
    return render_template("index.html", cars=CARS)

@app.route("/regg", methods=['POST'])
def regg():

    # validate vards
    vards = request.form.get('vards')
    if not vards:
        return render_template("error.html", msg="Missing vards")
    
    # validate car
    
    car = request.form.get("car")
    if not car:
        return render_template("error.html", msg="Missing car")
    if car not in CARS:
        return render_template("error.html", msg="Invalid car")

    # remember REGZ
    REGZ [vards] = car

    # confirm registration
    return redirect("/regg")

print(REGZ)

@app.route("/regg")
def regz():
    return render_template("registrs.html", regg=REGZ)

if __name__ == "__main__":
    app.run()
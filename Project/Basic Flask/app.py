from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        return render_template("result.html", name=name, age=age)
    return render_template("home.html")

app.run(debug=True)
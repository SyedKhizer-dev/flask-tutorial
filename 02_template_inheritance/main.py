from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return "<p>Welcome to Home!!!</p>"


@app.route("/home", methods=["Get"])
def home():
    return render_template("index.html")

@app.route("/contact",methods=["GET"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

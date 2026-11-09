from flask import Flask, render_template, request, redirect, url_for, jsonify

# creation of simple flask app

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Flask App!"


@app.route("/index", methods=["GET"])
def index():
    return "Welcome to index page"


# "Variable rules" are used to build URLs dynamically. The variable part is specified in the URL by marking it as <variable_name>.
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is: " + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is: " + str(score)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        print("Received form data:", request.form)

        maths = float(request.form["maths"])
        science = float(request.form["science"])
        english = float(request.form["english"])

        total_score = maths + science + english
        average_score = total_score / 3

        # return render_template(
        #     "form.html", total_score=total_score, average_score=average_score
        # )

        if average_score >= 40:
            res = "success"
        else:
            res = "fail"

        return redirect(url_for(res, score=average_score))


@app.route("/api", methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a_val = float(data["a"])
    b_val = float(data["b"])
    return jsonify({"sum": a_val + b_val})


if __name__ == "__main__":
    app.run(
        debug=True
    )  # "debug=True" will allow us to see the errors in the console if any error occurs

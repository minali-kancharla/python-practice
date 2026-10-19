from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        homework1 = float(request.form["homework1"])
        homework2 = float(request.form["homework2"])
        midterm = float(request.form["midterm"])
        project = float(request.form["project"])

        average = (homework1 + homework2 + midterm + project) / 4

    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

        return render_template(
            "index.html",
            average=average,
            letter_grade=letter_grade
        )

if __name__ == "__main__":
    app.run(debug=True)
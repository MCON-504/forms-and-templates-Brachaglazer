from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        if not name or name.strip() == "":
            error = "Name is required."
            name = None
        if not grade or not int(grade):
            error = "Grade is required."
            grade = None
        if int(grade) < 0 or int(grade) > 100:
            error = "Grade must be between 0 and 100."
            grade = None
        if not error:
            students.append({"name": name, "grade": grade})
            return redirect(url_for("display_students"))


    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    total_students = len(students)
    total_grades = 0
    max_grade = None
    min_grade = None
    if total_students > 0:
        for student in students:
            total_grades += int(student["grade"])
            if max_grade is None or int(student["grade"]) > max_grade:
                max_grade = int(student["grade"])
            if min_grade is None or int(student["grade"]) < min_grade:
                min_grade = int(student["grade"])

    return render_template("summary.html", total_students=total_students, total_grades=total_grades, min_grade=min_grade, max_grade=max_grade)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, flash
from core.storage import load_data, save_data
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

def get_data():
    return load_data()

def save(data):
    save_data(data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        data = get_data()
        user = next((u for u in data["users"] if u["email"] == email), None)
        if user and user.get("password") == password:
            session["user_id"] = user["user_id"]
            session["role"] = user["role"]
            session["name"] = user["name"]
            flash("Logged in successfully.")
            return redirect(url_for("index"))
        else:
            flash("Invalid email or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    data = get_data()
    if request.method == "POST":
        if session.get("role") != "Instructor":
            flash("Only instructors can add tasks.")
            return redirect(url_for("tasks"))
        title = request.form["title"]
        description = request.form["description"]
        course_name = request.form["course_name"]
        instructor_name = session.get("name", "Unknown")
        new_task = {
            "task_id": len(data.get("tasks", [])) + 1,
            "title": title,
            "description": description,
            "course_name": course_name,
            "instructor_name": instructor_name
        }
        data.setdefault("tasks", []).append(new_task)
        save(data)
        flash("Task added successfully.")
        return redirect(url_for("tasks"))
    # GET
    tasks = []
    for t in data.get("tasks", []):
        tasks.append({
            "title": t.get("title", ""),
            "description": t.get("description", ""),
            "course_name": t.get("course_name", "N/A"),
            "instructor_name": t.get("instructor_name", "N/A")
        })
    return render_template("tasks.html", tasks=tasks)

@app.route("/submissions", methods=["GET"])
def submissions():
    data = get_data()
    submissions = []
    for s in data.get("submissions", []):
        submissions.append({
            "id": s.get("id", ""),
            "student_name": s.get("student_name", ""),
            "task_title": s.get("task_title", ""),
            "content": s.get("content", ""),
            "grade": s.get("grade")
        })
    return render_template("submissions.html", submissions=submissions)

@app.route("/grade/<submission_id>", methods=["POST"])
def grade_submission(submission_id):
    data = get_data()
    grade = request.form.get("grade")
    for s in data.get("submissions", []):
        if str(s.get("id")) == str(submission_id):
            s["grade"] = int(grade)
            flash("Submission graded.")
            break
    save(data)
    return redirect(url_for("submissions"))

@app.route("/submit", methods=["GET", "POST"])
def submit():
    data = get_data()
    tasks = data.get("tasks", [])
    if request.method == "POST":
        task_id_raw = request.form.get("task_id", "")
        content = request.form.get("content", "")
        if not task_id_raw or not content:
            flash("Please select a task and enter your submission.")
            return render_template("submit.html", tasks=tasks)
        try:
            task_id = int(task_id_raw)
        except ValueError:
            flash("Invalid task selection.")
            return render_template("submit.html", tasks=tasks)
        user_id = session.get("user_id", "")
        user = next((u for u in data["users"] if u["user_id"] == user_id), None)
        task = next((t for t in tasks if int(t.get("task_id")) == task_id), None)
        if user and task:
            submission = {
                "id": len(data.get("submissions", [])) + 1,
                "student_name": user["name"],
                "task_title": task["title"],
                "content": content,
                "grade": None
            }
            data.setdefault("submissions", []).append(submission)
            save(data)
            flash("Submission successful.")
            return redirect(url_for("submissions"))
        else:
            flash("Invalid user or task.")
    return render_template("submit.html", tasks=tasks)
# Profile route to display user data after login
@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    data = get_data()
    user = next((u for u in data["users"] if u["user_id"] == session["user_id"]), None)
    return render_template("profile.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)

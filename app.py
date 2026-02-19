from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

from flask import Flask, render_template, request, redirect, url_for, session, flash
from core.storage import load_data, save_data
import os
from uuid import uuid4

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

def get_data():
    return load_data()

def save(data):
    save_data(data)

@app.route("/")
@login_required
def home():
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
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.route("/tasks", methods=["GET", "POST"])
@login_required
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
@login_required
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
@login_required
def grade_submission(submission_id):
    if session.get("role") != "Instructor":
        flash("Only instructors can grade submissions.")
        return redirect(url_for("submissions"))
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
@login_required
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

@app.route("/profile")
@login_required
def profile():
    data = get_data()
    user = next((u for u in data["users"] if u["user_id"] == session["user_id"]), None)
    return render_template("profile.html", user=user)
# Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    data = get_data()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]
        if any(u["email"] == email for u in data["users"]):
            flash("Email already registered.")
            return render_template("register.html")
        user_id = str(uuid4())
        user = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        data["users"].append(user)
        save(data)
        flash("Account created. Please login.")
        return redirect(url_for("login"))
    return render_template("register.html")

# Courses page: list, add, enroll
@app.route("/courses", methods=["GET", "POST"])
@login_required
def courses():
    data = get_data()
    user_id = session.get("user_id")
    role = session.get("role")
    user = next((u for u in data["users"] if u["user_id"] == user_id), None)
    if request.method == "POST" and role == "Instructor":
        course_name = request.form["course_name"]
        course_id = str(uuid4())
        new_course = {
            "course_id": course_id,
            "course_name": course_name,
            "instructor_id": user_id,
            "students": [],
            "tasks": []
        }
        data.setdefault("courses", []).append(new_course)
        save(data)
        flash("Course added successfully.")
        return redirect(url_for("courses"))
    # GET: list courses
    courses = []
    for c in data.get("courses", []):
        instructor = next((u for u in data["users"] if u["user_id"] == c["instructor_id"]), None)
        enrolled = False
        if role == "Student" and user:
            enrolled = c["course_id"] in (user.get("courses") or [])
        courses.append({
            "course_id": c["course_id"],
            "course_name": c["course_name"],
            "instructor_name": instructor["name"] if instructor else "Unknown",
            "enrolled": enrolled
        })
    return render_template("courses.html", courses=courses)

# Student enrolls in a course
@app.route("/enroll", methods=["POST"])
@login_required
def enroll():
    data = get_data()
    user_id = session.get("user_id")
    course_id = request.form.get("course_id")
    user = next((u for u in data["users"] if u["user_id"] == user_id), None)
    course = next((c for c in data.get("courses", []) if c["course_id"] == course_id), None)
    if not user or not course or user["role"] != "Student":
        flash("Invalid enrollment request.")
        return redirect(url_for("courses"))
    if "courses" not in user:
        user["courses"] = []
    if course_id not in user["courses"]:
        user["courses"].append(course_id)
    if "students" not in course:
        course["students"] = []
    if user_id not in course["students"]:
        course["students"].append(user_id)
    save(data)
    flash("Enrolled in course successfully.")
    return redirect(url_for("courses"))

if __name__ == "__main__":
    app.run(debug=True)

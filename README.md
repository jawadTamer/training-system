# Training System – Layered Flask & OOP Architecture

## 📌 Overview

The Training System is a layered Python application that demonstrates both:

1. A Flask-based web application interface  
2. A pure Python object-oriented system simulation  

The project follows a structured architecture separating models, services, database handling, and presentation layers.

It is designed for educational purposes to demonstrate clean project organization, role-based logic, and persistent JSON storage.

---

## 🚀 Features

- Role-based system (Student / Instructor)
- Course creation and enrollment
- Task creation and management
- Student task submission
- Instructor grading system
- JSON-based persistent storage
- Flask web interface
- Standalone OOP system simulation via CLI

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Jinja2 Templates
- JSON file storage
- Object-Oriented Programming principles

---

## 🏗️ Architecture Overview

The project follows a layered design:

- **Models Layer** → Represents entities (User, Student, Instructor, Course, Task, Submission)
- **Services Layer** → Business logic and system orchestration
- **Database Layer** → JSON storage handling
- **Presentation Layer** → Flask routes and HTML templates

---

## 📂 Project Structure

```
training-system/
│
├── app.py                     # Flask web application entry point
├── main.py                    # Standalone OOP system simulation
├── requirements.txt           # Project dependencies
├── README.md
│
├── core/
│   ├── __init__.py
│   └── storage.py
│
├── database/
│   ├── __init__.py
│   └── json_storage.py        # JSON persistence layer
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── instructor.py
│   ├── courses.py
│   ├── task.py
│   └── submission.py
│
├── services/
│   ├── __init__.py
│   └── system_manager.py      # Core business logic controller
│
├── templates/                 # Flask HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── courses.html
│   ├── tasks.html
│   ├── submit.html
│   └── submissions.html
│
├── data/
│   └── data.json              # Application data storage
│
└── venv/                      # Virtual environment (should not be committed)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jawadTamer/training-system.git
cd training-system
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🌐 Run the Flask Web Application

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

This launches the browser-based training management system.

---

### 🧪 Run the Standalone OOP Simulation

```bash
python main.py
```

This executes a full example workflow:

- Creates instructor
- Creates course
- Creates student
- Enrolls student
- Creates task
- Submits solution
- Grades submission
- Saves system state to JSON

This demonstrates the architecture independent of Flask.

---

## 💾 Data Storage

All persistent data is stored in:

```
data/data.json
```

The JSON storage layer is handled by:

```
database/json_storage.py
```

This approach is suitable for educational and small-scale projects.  
For production systems, a relational database is recommended.

---

## 🔐 Recommended Improvements

- Add password hashing (e.g., using `werkzeug.security`)
- Replace JSON storage with a relational database
- Add input validation and error handling
- Implement RESTful API endpoints
- Add authentication decorators for role-based access
- Remove `venv/` from version control and add `.gitignore`

---

## 📄 License

This project is intended for educational and demonstration purposes.

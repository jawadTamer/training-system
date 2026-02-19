# Training System

A comprehensive web-based training and course management system built with Python, Flask, and object-oriented design principles. This project demonstrates a layered architecture separating models, services, database handling, and presentation layers.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Architecture](#architecture)
- [API & Routes](#api--routes)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The Training System is a dual-interface Python application that serves both as:

1. **Flask Web Application** - A browser-based interface for managing courses, tasks, and submissions
2. **Standalone OOP System** - A pure Python simulation demonstrating clean architecture principles

Designed for educational purposes, this project showcases modern software engineering practices including role-based access control, persistent JSON storage, and separation of concerns.

---

## 🚀 Features

### Core Functionality
- **Role-Based Access Control** - Separate workflows for Students and Instructors
- **Course Management** - Create, manage, and enroll in courses
- **Task Management** - Create assignments and track submissions
- **Submission System** - Students submit solutions; instructors review and grade
- **User Profiles** - Manage user information and roles
- **Persistent Storage** - JSON-based data persistence

### Security & Access
- Session-based authentication
- Role-based route protection
- User profile management

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask 3.1.2 |
| **Template Engine** | Jinja2 |
| **Data Storage** | JSON files |
| **Server** | Werkzeug 3.1.5 |
| **Language** | Python 3.7+ |
| **Database** | JSON (development) |

---

## 📂 Project Structure

```
training-system/
│
├── app.py                          # Flask web application entry point
├── main.py                         # Standalone OOP system simulation
├── requirements.txt                # Project dependencies
├── README.md                       # This file
│
├── core/
│   ├── __init__.py
│   └── storage.py                  # Data loading and saving utilities
│
├── database/
│   ├── __init__.py
│   └── json_storage.py             # JSON persistence layer
│
├── models/                         # Entity models
│   ├── __init__.py
│   ├── user.py                     # Base User class
│   ├── student.py                  # Student model with enrollment logic
│   ├── instructor.py               # Instructor model with management logic
│   ├── courses.py                  # Course model
│   ├── task.py                     # Task/Assignment model
│   └── submission.py               # Student submission model
│
├── services/
│   ├── __init__.py
│   └── system_manager.py           # Core business logic & orchestration
│
├── templates/                      # Flask HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home page
│   ├── login.html                  # User login
│   ├── register.html               # User registration
│   ├── profile.html                # User profile page
│   ├── courses.html                # Courses listing
│   ├── tasks.html                  # Tasks view
│   ├── submit.html                 # Task submission form
│   └── submissions.html            # View/grade submissions
│
├── data/
│   └── data.json                   # Application data storage
│
├── static/                         # Static files (CSS, JS, images)
│   └── style.css                   # Application styling
│
└── venv/                           # Virtual environment (not committed)
```

---

## ⚙️ Installation & Setup

### Prerequisites

- **Python 3.7** or higher
- **pip** (Python package manager)
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/jawadTamer/training-system.git
cd training-system
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output: All packages from `requirements.txt` will be installed.

---

## 🚀 Getting Started

### Run the Flask Web Application

```bash
python app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Run the Standalone OOP Simulation

```bash
python main.py
```

This executes a complete workflow demonstrating the system architecture:
- Creates an instructor and student
- Creates a course and enrolls the student
- Creates a task within the course
- Processes a task submission
- Grades the submission
- Saves all data to JSON

---

## 💡 Usage

### Default Test Accounts

The system comes with pre-loaded test accounts (located in `data/data.json`):

**Instructor Account:**
- Email: `ahmed@mail.com`
- Password: `instructor123`

**Student Account:**
- Email: `ali@mail.com`
- Password: `student123`

### Key Features Walkthrough

#### For Students
1. **Login** - Access your account with email and password
2. **Browse Courses** - View available courses and enroll
3. **View Tasks** - See assignments within your enrolled courses
4. **Submit Work** - Upload solutions to course tasks
5. **Track Progress** - View feedback and grades from instructors

#### For Instructors
1. **Login** - Access your instructor dashboard
2. **Create Courses** - Set up new training programs
3. **Create Tasks** - Define assignments for courses
4. **Review Submissions** - View and grade student work
5. **Manage Students** - See enrolled students and their progress

---

## 🏗️ Architecture

### Layered Design Pattern

The application follows a layered architecture for clean separation of concerns:

```
┌─────────────────────────────┐
│   Presentation Layer        │  ← Flask routes, HTML templates
├─────────────────────────────┤
│   Service Layer             │  ← Business logic (TrainingSystem)
├─────────────────────────────┤
│   Model Layer               │  ← Entity classes (User, Course, etc.)
├─────────────────────────────┤
│   Database Layer            │  ← JSON storage, data persistence
└─────────────────────────────┘
```

### Model Overview

**User Hierarchy:**
```
User (Base Class)
├── Student
└── Instructor
```

**Core Models:**
- **Course** - Training program with description and instructor
- **Task** - Assignment within a course
- **Submission** - Student's task solution with feedback

### Service Layer

**TrainingSystem** (`services/system_manager.py`):
- Manages users, courses, and tasks
- Handles enrollment and submissions
- Orchestrates data persistence

---

## 🌐 API & Routes

### Authentication Routes
- `GET /` - Home page / Dashboard
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /register` - Registration page
- `POST /register` - Create new account
- `GET /logout` - Logout user

### User Routes
- `GET /profile` - View user profile
- `POST /profile` - Update user information

### Course Routes
- `GET /courses` - List all courses
- `POST /enroll/<course_id>` - Enroll in a course

### Task Routes
- `GET /tasks` - View tasks for enrolled courses
- `GET /tasks/<task_id>` - View task details

### Submission Routes
- `GET /submit/<task_id>` - Submission form
- `POST /submit/<task_id>` - Submit solution
- `GET /submissions` - View all submissions (for instructors)
- `POST /grade/<submission_id>` - Grade submission

---

## 💾 Data Storage

All application data is persisted in JSON format:

```json
{
  "users": [...],
  "courses": [...],
  "tasks": [...],
  "submissions": [...]
}
```

**Storage Location:** `data/data.json`

**Handler:** `database/json_storage.py`

### Loading Data
```python
from database.json_storage import load_data
data = load_data()
```

### Saving Data
```python
from database.json_storage import save_data
save_data(system.get_state())
```

---

## 🔧 Configuration

### Environment Variables

Set these optional environment variables:

```bash
# Flask Configuration
export FLASK_ENV=development
export FLASK_DEBUG=True
export SECRET_KEY=your-secret-key-here
```

**Default Secret Key:** `dev-secret-key` (change in production)

---

## 🔐 Security Recommendations

For production deployment, implement the following:

1. **Password Hashing**
   ```python
   from werkzeug.security import generate_password_hash, check_password_hash
   ```

2. **Database Migration**
   - Replace JSON with PostgreSQL or MySQL
   - Use SQLAlchemy ORM for better data management

3. **Input Validation**
   - Add WTForms for form validation
   - Implement CSRF protection

4. **Authentication**
   - Implement JWT tokens
   - Add Flask-Login for session management

5. **Error Handling**
   - Add comprehensive error pages (404, 500, etc.)
   - Implement logging

6. **Version Control**
   - Add `.gitignore` to exclude `venv/` and `__pycache__/`

---

## 📦 Dependencies

See `requirements.txt` for the complete list:

```
Flask==3.1.2
Werkzeug==3.1.5
Jinja2>=3.0
MarkupSafe>=2.0
click>=8.0
blinker>=1.4
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to classes and methods

---

## 📚 Learning Resources

This project demonstrates:
- Object-Oriented Programming (OOP) principles
- Layered architecture patterns
- MVC (Model-View-Controller) concepts
- Flask web framework fundamentals
- JSON data persistence
- Role-based access control

---

## 🚀 Future Enhancements

- [ ] Database migration to PostgreSQL/MySQL
- [ ] User registration with email verification
- [ ] Password hashing and reset functionality
- [ ] Real-time notifications
- [ ] File upload support for submissions
- [ ] Progress tracking and analytics
- [ ] RESTful API with Swagger documentation
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] Deployment documentation (Heroku, AWS, etc.)

---

## 📄 License

This project is open source and available for educational and demonstration purposes.

---

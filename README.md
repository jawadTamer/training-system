<<<<<<< HEAD
# Training System

A web-based training and course management system built with Flask. This application enables instructors to create and manage courses while students can enroll, view tasks, and submit assignments.

## Features

- **User Authentication**: Login system with role-based access (Student/Instructor)
- **Course Management**: Instructors can create and manage courses
- **Task Management**: Create, assign, and track tasks within courses
- **Submissions**: Students can submit task solutions and instructors can review them
- **User Profiles**: View and manage user information
- **JSON-based Storage**: Persistent data storage using JSON files

## Project Structure

```
training-system/
├── app.py                 # Main Flask application and routes
├── main.py               # Additional application entry point
├── requirements.txt      # Python dependencies
├── data/
│   └── data.json         # JSON data storage
├── core/
│   ├── __init__.py
│   └── storage.py        # Data loading and saving functions
├── database/
│   ├── __init__.py
│   └── json_storage.py   # JSON storage handler
├── models/
│   ├── __init__.py
│   ├── user.py          # Base User class
│   ├── student.py       # Student model
│   ├── instructor.py    # Instructor model
│   ├── courses.py       # Course model
│   ├── task.py          # Task model
│   └── submission.py    # Submission model
├── services/
│   ├── __init__.py
│   └── system_manager.py # Core training system logic
└── templates/           # HTML templates
    ├── base.html        # Base template
    ├── index.html       # Home page
    ├── login.html       # Login page
    ├── register.html    # Registration page
    ├── profile.html     # User profile
    ├── courses.html     # Courses list
    ├── tasks.html       # Tasks page
    ├── submit.html      # Task submission
    └── submissions.html # View submissions
```

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone or download the project:
```bash
cd training-system
```

2. Install required dependencies:
=======
<p align="">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:9333EA&height=180&section=header&text=Training%20System&fontSize=40&fontColor=ffffff&animation=fadeIn"/>
</p>

<p align="">
  <b>A comprehensive web-based training and course management system</b><br>
  Built with Python, Flask, and object-oriented design principles.
</p>

<p align="">

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)
![Werkzeug](https://img.shields.io/badge/Werkzeug-3.1.5-lightgrey)
![Jinja2](https://img.shields.io/badge/Jinja2-Template-red?logo=jinja)
![Architecture](https://img.shields.io/badge/Architecture-Layered-blueviolet)
![Storage](https://img.shields.io/badge/Storage-JSON-orange)
![Status](https://img.shields.io/badge/Project-Active-success)

</p>

---

## 📋 Table of Contents

<p align="center">

<a href="#-overview">
  <img src="https://img.shields.io/badge/🎯%20Overview-111111?style=for-the-badge&logoColor=white" />
</a>
<a href="#-features">
  <img src="https://img.shields.io/badge/🚀%20Features-0A66C2?style=for-the-badge&logoColor=white" />
</a>
<a href="#️-tech-stack">
  <img src="https://img.shields.io/badge/🛠️%20Tech%20Stack-FF6F00?style=for-the-badge&logoColor=white" />
</a>
<a href="#-project-structure">
  <img src="https://img.shields.io/badge/📂%20Project%20Structure-6A1B9A?style=for-the-badge&logoColor=white" />
</a>

<a href="#️-installation">
  <img src="https://img.shields.io/badge/⚙️%20Installation-00897B?style=for-the-badge&logoColor=white" />
</a>
<a href="#-getting-started">
  <img src="https://img.shields.io/badge/🚀%20Getting%20Started-2E7D32?style=for-the-badge&logoColor=white" />
</a>
<a href="#-usage">
  <img src="https://img.shields.io/badge/💡%20Usage-F9A825?style=for-the-badge&logoColor=white" />
</a>
<a href="#️-architecture">
  <img src="https://img.shields.io/badge/🏗️%20Architecture-455A64?style=for-the-badge&logoColor=white" />
</a>


<a href="#-api--routes">
  <img src="https://img.shields.io/badge/🌐%20API%20%26%20Routes-1565C0?style=for-the-badge&logoColor=white" />
</a>
<a href="#-contributing">
  <img src="https://img.shields.io/badge/🤝%20Contributing-43A047?style=for-the-badge&logoColor=white" />
</a>
<a href="#-license">
  <img src="https://img.shields.io/badge/📄%20License-C62828?style=for-the-badge&logoColor=white" />
</a>

</p>

---

# 🎯 Overview

The Training System is a dual-interface Python application that serves both as:

| Feature | Description |
|---------|------------|
| 💻 **Flask Web Application** | A browser-based interface for managing courses, tasks, and submissions |
| ⚙️ **Standalone OOP System** | A pure Python simulation demonstrating clean architecture principles |
| 🏗️ **Modern Practices** | Role-based access control, persistent JSON storage, and separation of concerns |

---

<p align="center">
  <img src="https://img.shields.io/badge/Flask-Web%20App-4F46E5?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Practices-Secure-9333EA?style=for-the-badge&logoColor=white" />
</p>



---

# 🚀 Features

## ✨ Core Functionality

![Course Management](https://img.shields.io/badge/Course_Management-Create%2C%20Enroll-blue?style=for-the-badge&logo=book&logoColor=white)
![Task Management](https://img.shields.io/badge/Task_Management-Assignments%20%26%20Tracking-8B5CF6?style=for-the-badge&logo=tasks&logoColor=white)
![User Profiles](https://img.shields.io/badge/User_Profiles-Manage%20Info-yellow?style=for-the-badge&logo=account&logoColor=black)
![Persistent Storage](https://img.shields.io/badge/Persistent_Storage-JSON-orange?style=for-the-badge&logo=json&logoColor=white)

## 🔐 Security & Access

![Session Auth](https://img.shields.io/badge/Session_Authentication-Active-red?style=for-the-badge&logo=key&logoColor=white)
![User Profile Management](https://img.shields.io/badge/User_Profile_Management-Enabled-6366F1?style=for-the-badge&logo=account&logoColor=white)

---

# 🛠️ Tech Stack
<p align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JS-F7DF1E?logo=javascript&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?logo=visual-studio-code&logoColor=white)

</p>




<p align="center">
| Layer        | Technology Used |
|--------------|----------------|
| Backend      | Python, Flask  |
| Templating   | Jinja2         |
| Server Core  | Werkzeug       |
| Storage      | JSON           |
| Architecture | Layered & OOP  |
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3"/>
</p>
# 📂 Project Structure

<p align="center">


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

>>>>>>> 7b9b9020ea5510f7e5b7d48fa65b124736b7cf09
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
## Running the Application

### Using Flask
```bash
flask run
```

### Using Python directly
=======
Expected output: All packages from `requirements.txt` will be installed.

---

## 🚀 Getting Started

### Run the Flask Web Application

>>>>>>> 7b9b9020ea5510f7e5b7d48fa65b124736b7cf09
```bash
python app.py
```

<<<<<<< HEAD
The application will be available at `http://localhost:5000`

## Usage

### Login Credentials

Default test accounts (found in `data/data.json`):

**Instructor:**
- Email: `ahmed@mail.com`
- Password: `instructor123`

**Student:**
- Email: `ali@mail.com`
- Password: `student123`

### Key Features

1. **Dashboard**: View enrolled courses and recent tasks after login
2. **Courses**: Browse and enroll in available courses
3. **Submit Tasks**: Students can submit solutions to course tasks
4. **Profile**: View and update user information
5. **Course Management**: Instructors can create and manage courses

## Database

Data is stored in JSON format in `data/data.json`. The system includes:
- Users (Students and Instructors)
- Courses and their details
- Tasks within courses
- Student submissions

## Technology Stack

- **Backend**: Flask 3.1.2
- **Frontend**: HTML/Jinja2 Templates
- **Data Storage**: JSON
- **Server**: Werkzeug 3.1.5

## Dependencies

See `requirements.txt` for the complete list of dependencies:
- Flask - Web framework
- Jinja2 - Template engine
- Werkzeug - WSGI utility library
- Click - CLI utilities
- Blinker - Signal support
- MarkupSafe - String escaping

## Project Architecture

### Models
- **User**: Base user class with common properties
- **Student**: Extends User, handles course enrollment and task submissions
- **Instructor**: Extends User, manages courses and tasks
- **Course**: Represents a training course
- **Task**: Represents course assignments
- **Submission**: Student task submissions

### Services
- **TrainingSystem**: Core business logic for managing users, courses, and tasks

### Storage
- **core/storage.py**: Functions for loading and saving data
- **database/json_storage.py**: JSON file handling

## Development Notes

- The application uses session-based authentication
- Secret key is configurable via `SECRET_KEY` environment variable (defaults to "dev-secret-key")
- All data is persisted to `data/data.json`

## Future Enhancements

- Database migration to a relational database
- User registration feature
- Email notifications
- Progress tracking and grades
- File upload support for submissions
- Real-time collaboration features

## License

This project is open source and available for educational purposes.
=======
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

<p align="">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:9333EA&height=80&section=footer"/>
</p>
>>>>>>> 7b9b9020ea5510f7e5b7d48fa65b124736b7cf09

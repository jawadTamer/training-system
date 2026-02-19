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
```bash
pip install -r requirements.txt
```

## Running the Application

### Using Flask
```bash
flask run
```

### Using Python directly
```bash
python app.py
```

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

import uuid

class TrainingSystem:
    def __init__(self):
        self.users = []
        self.courses = []

    # ---------------- USERS ----------------
    def add_user(self, user):
        if self.get_user_by_id(user.user_id):
            raise ValueError("User ID already exists.")
        self.users.append(user)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    # ---------------- COURSES ----------------
    def add_course(self, course):
        if self.get_course_by_id(course.course_id):
            raise ValueError("Course ID already exists.")
        self.courses.append(course)

    def get_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    # ---------------- SEARCH ----------------
    def list_students(self):
        return [u for u in self.users if u.role == "Student"]

    def list_instructors(self):
        return [u for u in self.users if u.role == "Instructor"]

    def generate_id(self):
        return str(uuid.uuid4())
from models.user import User
from models.submission import Submission

class Student(User):
    '''Student class inherits from User Represents a student in the training system'''
    def __init__(self, user_id, name, email, password=None):
        '''Constructor: initializes student with basic info and courses'''
        super().__init__(user_id, name, email, password)
        self.role = "Student"
        self.courses = []

    def enroll_course(self, course):
        '''Enrolls the student in a course.'''
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")

    def submit_task(self, task, content):
        '''Creates a Submission object and links it to the task.'''
        if task not in [t for course in self.courses for t in course.tasks]:
            raise ValueError("You are not enrolled in this course.")

        new_submission = Submission(task, self, content)
        task.submissions.append(new_submission)
        return new_submission
    

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["courses"] = [course.course_id for course in self.courses]
        return user_dict
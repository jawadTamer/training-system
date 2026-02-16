from models.user import User
from models.task import Task        
        
class Instructor(User):
    '''Instructor class inherits from User.'''

    def __init__(self, user_id, name, email, password=None):
        '''Constructor: initializes instructor with basic info'''
        super().__init__(user_id, name, email, password)
        self.role = "Instructor"

    def create_task(self, course, title, description):
        '''Creates a new Task object and adds it to a specific course.'''
        new_task = Task(title, description, self)
        
        course.add_task(new_task)
        
        print(f"Instructor {self.name} created task: '{title}' for course: {course.course_name}")
        return new_task

    def grade_submission(self, submission, grade):
        '''Assigns a grade to a specific student submission.'''
        if submission.task.instructor != self:
            raise PermissionError("You cannot grade this task.")
        
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")

        submission.grade = grade

    def to_dict(self):
        return super().to_dict()
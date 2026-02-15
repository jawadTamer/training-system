from models.user import User

class Instructor(User):
    '''Instructor class inherits from User
    Represents an instructor in the training system'''

    def __init__(self, user_id, name, email):
        ''' Constructor: initializes instructor with basic info'''
        super().__init__(user_id, name, email)
        self.role = "Instructor"


    def create_task(self, task_name):
        ''' Create a new task/assignment'''
        print(f"Instructor {self.name} created task: {task_name}")

    
    def grade_student(self, student_name, grade):
        '''Grade a student's task'''
        print(f"{self.name} graded {student_name} with {grade}")

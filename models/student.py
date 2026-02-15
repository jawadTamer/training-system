from models.user import User

class Student(User):
    '''
    Student class inherits from User
    Represents a student in the training system
    '''


    def __init__(self, user_id, name, email):
        '''Constructor: initializes student with 
            basic info and an empty list of courses'''
        super().__init__(user_id, name, email)
        self.role = "Student"
        self.courses = []


    def enroll_course(self, course):
        '''Enroll the student in a new course'''
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
        
    def submit_task(self, task_name):
        '''Submit a task for a course '''
        print(f"{self.name} submitted task: {task_name}")
    

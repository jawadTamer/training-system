from models.student import Student

class Course:
    '''Course base class represents any system usecourser (ML, Gen AI, etc.)'''
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.students = []
        self.tasks = []

    def add_student(self, student):
        '''Adds a student to the course and links the course to the student.'''
        if student not in self.students :
            self.students.append(student)
            student.enroll_course(self)
            print(f"Student {student.name} added to {self.course_name} course.")

    def add_task(self, task):
        '''Adds a task to the course curriculum.'''
        self.tasks.append(task)
        print(f"New task {task.title} added to {self.course_name}.")

    def __str__(self):
        return f"Course: {self.course_name} | Instructor: {self.instructor.name}"
    
    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "instructor_id": self.instructor.user_id,
            "students": [student.user_id for student in self.students],
            "tasks": [task.task_id for task in self.tasks]
        }
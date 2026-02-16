from services.system_manager import TrainingSystem
from models.student import Student
from models.instructor import Instructor
from models.courses import Course
from database.json_storage import JSONStorage

system = TrainingSystem()

# Create Instructor
instructor = Instructor(system.generate_id(), "Ahmed", "ahmed@mail.com")
system.add_user(instructor)

# Create Course
course = Course(system.generate_id(), "Machine Learning", instructor)
system.add_course(course)

# Create Student
student = Student(system.generate_id(), "Ali", "ali@mail.com")
system.add_user(student)

# Enroll Student
course.add_student(student)

# Instructor creates task
task = instructor.create_task(course, "HW1", "Linear Regression")

# Student submits
submission = student.submit_task(task, "My solution")

# Instructor grades
instructor.grade_submission(submission, 95)

JSONStorage.save(system)
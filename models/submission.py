class Submission:
    def __init__(self, task, student, content):
        """
        Initialize a Submission object[cite: 41].
        :param task: The Task object associated with this submission.
        :param student: The Student object who made the submission.
        :param content: The actual content or solution provided.
        """
        self.task = task           # The associated task 
        self.student = student     # The student who submitted 
        self.content = content     # The content of the submission 
        self.grade = None          # Grade is initialized as None 

    def __str__(self):
        return f"Submission by {self.student.name} for {self.task.title}"
    
    def to_dict(self):
        return {
            "task_id": self.task.task_id,
            "student_id": self.student.user_id,
            "content": self.content,
            "grade": self.grade
        }
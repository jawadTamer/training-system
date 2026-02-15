import uuid

class Task:

    """Task class represents any task in the system, such as assignments, projects, or to-dos."""


    def __init__(self,title,description,instructor):
        """Constructor: initializes basic task information"""
        self.task_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.instructor = instructor
        self.submissions = []
        # Removed dependency on load_data for simplicity in this test.
        # In a real application, you might use a counter or a UUID for task_id.
        self.task_id = self._generate_task_id()

    def _generate_task_id(self):
        # Simple placeholder for generating a unique task ID.
        # In a production system, this would be more robust.
        return hash(self.title + self.description + self.instructor.name)


    def __str__(self):
        return f"Task: {self.title}\nTask ID: {self.task_id}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "instructor_id": self.instructor.user_id,
            "submissions": [submission.to_dict() for submission in self.submissions]
        }
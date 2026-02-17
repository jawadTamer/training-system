from core.storage import load_data

class Task:
    
    """Task class represents any task in the system, such as assignments, projects, or to-dos."""
    
           
    def __init__(self,title,description,instructor):
        """Constructor: initializes basic task information""" 
        
        self.title = title
        self.description = description
        self.instructor = instructor
        self.submissions = []
        
    data = load_data()
    Tasks = data.get("tasks", [])     
    task_id = len(Tasks) + 1  
    
       
    def __str__(self):
        return f"Task{self.title}\nTask ID:{self.task_id}"
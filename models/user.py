class User:
    '''User base class represents any system user (Student, Instructor, etc.)'''
    def __init__(self, user_id, name, email):
        '''Constructor: initializes basic user information'''
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = "User"

    def display_info(self):
        '''Displays all user details'''
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")

    
    def login(self):
        '''Simulates user login action'''
        print(f"{self.name} logged in successfully.")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }
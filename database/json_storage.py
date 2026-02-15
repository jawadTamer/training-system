import json
import os

class JSONStorage:

    @staticmethod
    def save(system, filename="data.json"):
        # Get root directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")

        # Create data folder if not exists
        os.makedirs(data_dir, exist_ok=True)

        file_path = os.path.join(data_dir, filename)

        data = {
            "users": [user.to_dict() for user in system.users],
            "courses": [course.to_dict() for course in system.courses]
        }

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(filename="data.json"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "data", filename)

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r") as f:
            return json.load(f)

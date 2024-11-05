from .exceptions import *

class User:
    id : int
    username: str
    email: str
    
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email
    
    def is_valid(self):
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise InvalidEmailFormat("Invalid email format")
    

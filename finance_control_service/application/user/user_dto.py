from dataclasses import dataclass

@dataclass
class UserDTO(object):
    id: int
    email: str
    first_name: str | None
    last_name: str | None

    def __init__(self, id: int, email: str, first_name: str = None, last_name: str = None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

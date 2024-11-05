class UserDto(object):
    id: int
    username: str
    email: str

    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email
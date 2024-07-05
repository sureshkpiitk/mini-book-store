from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    username: str
    name: str
    dob: datetime.date


class UserManager:

    def __init__(self):
        self.users: dict[str, User] = {}

    def register(self, username: str, name: str, dob: str):
        if username in self.users:
            return self.users[username]
        new_user = User(username, name, datetime.strptime(dob, "%Y-%m-%d").date())
        self.users[username] = new_user
        return new_user

    def display(self):
        for user in self.users.values():
            print(user)

    def get_a_user_with_username(self, username: str):
        return self.users.get(username)


UserManagerObj = UserManager()

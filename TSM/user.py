
class User:
    def __init__(self, username, email, role):
        self._username = username
        self._email = email
        self._role = role
        self._tasks = []

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    def assign_task(self, task):
        self._tasks.append(task)

    def get_tasks(self):
        return self._tasks

    def __str__(self):
        return f"User(username={self.username}, role={self.role})"

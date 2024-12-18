from datetime import datetime

class Task:
    STATUS_OPTIONS = ["To Do", "In Progress", "Completed"]

    def __init__(self, title, description, due_date, priority="Medium"):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority
        self.status = "To Do"
        self.assigned_to = None

    def update_status(self, status):
        if status not in self.STATUS_OPTIONS:
            raise ValueError(f"Invalid status: {status}")
        self.status = status

    def assign_to(self, user):
        self.assigned_to = user
        user.assign_task(self)

    def is_overdue(self):
        return datetime.now() > self.due_date

    def __str__(self):
        return (f"Task(title={self.title}, status={self.status}, "
                f"assigned_to={self.assigned_to.username if self.assigned_to else None})")


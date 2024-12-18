import slash
from ..user import User
from ..task import Task

@slash.parametrize("status", ["To Do", "In Progress", "Completed"])
def test_task_status_update(status):
    task = Task("Test Task", "Description", "2024-12-15")
    task.update_status(status)
    assert task.status == status

def test_assign_task_to_user():
    user = User("testuser", "test@example.com", "Developer")
    task = Task("Task for User", "Details", "2024-12-10")
    task.assign_to(user)
    assert task.assigned_to == user
    assert task in user.get_tasks()

def test_task_overdue():
    task = Task("Old Task", "Past due", "2023-01-01")
    assert task.is_overdue() is True

def test_invalid_status_update():
    task = Task("Task", "Details", "2024-12-15")
    with slash.assert_raises(ValueError):
        task.update_status("InvalidStatus")
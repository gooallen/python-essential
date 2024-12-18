from user import User
from task import Task
from team import Team

def main():
    admin = User("admin", "admin@example.com", "Admin")
    manager = User("manager", "manager@example.com", "Manager")
    developer = User("dev", "dev@example.com", "Developer")

    team = Team("Devloperment Team")
    team.add_member(manager)
    team.add_member(developer)

    task1 = Task("Fix Bug #101", "Fix critical bug in module A", "2024-12-15")
    task2 = Task("Develop Feature X", "Build feature X as per spec", "2024-12-20")

    task1.assign_to(developer)
    task2.assign_to(manager)

    print(task1)
    print(task2)
    print(team)

if __name__ == "__main__":
    main()
        

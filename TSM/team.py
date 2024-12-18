
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        self.members.append(user)

    def remove_member(self, user):
        self.members.remove(user)

    def get_members(self):
        return self.members

    def __str__(self):
        return f"Team(name={self.name}, members={[member.username for member in self.members]})"
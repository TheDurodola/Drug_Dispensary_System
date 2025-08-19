class Admins:
    def __init__(self):
        self.admins = []

    def count(self):
        return len(self.admins)

    def addAdmin(self, admin: Admin):
        self.admins.append(admin)
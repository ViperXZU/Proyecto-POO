from datetime import datetime

class User:
    def __init__(self, username, email="", password="", create_time=datetime.now()):
        self.username = username
        self.email = email
        self.password = password
        self.create_time = create_time

    def __str__(self):
        return "{0} {1} {2}".format(self.username, self.email, self.create_time)

    def getUsername(self):
        return self.username

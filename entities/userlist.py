
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\n"

    def __repr__(self):
        return "User(name=%s, age=%s)" % (self.name, self.age)

class Users:
    def __init__(self):
        self.users = list()

    def AddUser(self, user):
        self.users.append(user)

    # Returns the array contents
    def GetUsers(self):
        return self.users

    def __str__(self):
        return "Number of users: {0}" \
            .format(str(len(self.users)))

    def __repr__(self):
        return "Users()"
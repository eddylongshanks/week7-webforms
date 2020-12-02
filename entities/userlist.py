
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
        self.counter = 0

    def AddUser(self, user):
        user.id = self.counter
        self.users.append(user)
        # Counter will always increase, even after deleting an item, therefore will always be unique
        self.counter += 1

    def DeleteUser(self, id):
        for index, user in enumerate(self.users):
            if user.id == id:
                del self.users[index]
    
    def GetUsers(self):
        return self.users

    def __str__(self):
        return "Number of users: {0}" \
            .format(str(len(self.users)))

    def __repr__(self):
        return "Users()"
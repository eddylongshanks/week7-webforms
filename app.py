from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
        # Check for the type of the object to determine admin status        
        self.users.append(user)

    # Returns the array contents
    def GetUsers(self):
        return self.users

    def __str__(self):
        return "There are {0} users" \
            .format(str(len(self.users)))

    def __repr__(self):
        return "Users()"

class FieldNameProvider:
    # Provides the function to return a display-friendly name for the error summary in the View
    def __init__(self):
        self.names = {
            "first-name" : "Name",
            "age" : "Age"
        }
    
    def get_name(self, field_name):
        return self.names[field_name]
    
    def __str__(self):
        return "A dictionary of display-friendly field names, use get_name([field_name]) to access"

    def __repr__(self):
        return "FieldNameProvider()"


users = Users()

@app.route("/")
def home():
    userlist = users.GetUsers()
    return render_template("index.html", users=userlist)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        _form = request.form

        errors = get_errors(_form)

        if errors:            
            return render_template("add_user.html", error_summary=errors)

        new_user = User(_form["first-name"], _form["age"])

        users.AddUser(new_user)

        return redirect("/")
        
    return render_template("add_user.html")

def get_errors(form_to_validate):
        invalid_input = list()

        field_name_provider = FieldNameProvider()

        for i, k in form_to_validate.items():
            if k == "":
                invalid_input.append(field_name_provider.get_name(i))
        
        if invalid_input:
            error_summary = f"Following information is required: {', '.join(invalid_input)}"
            return error_summary
        
app.run(debug=True)



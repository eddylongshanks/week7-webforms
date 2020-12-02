from entities.userlist import Users
from entities.userlist import User
from helpers.providers import FieldNameProvider
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
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


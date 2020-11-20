from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Temp redirect
    return add_user()

@app.route("/add_user")
def add_user():
    return render_template("add_user.html")

app.run(debug=True)
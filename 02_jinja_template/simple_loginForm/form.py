from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "amraha123" and password == "password":
    #     return render_template("welcome.html", name = username)
    
    # if we have multiple credentials
    credentials = {
        "admin" : "123",
        "amraha" : "amr123",
        "abc" : "xyz"
    }

    if username in credentials and password == credentials[username]:
        return render_template("welcome.html")
    else:
        return "Oops! Invalid credentials :("
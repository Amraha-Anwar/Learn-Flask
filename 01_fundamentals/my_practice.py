from flask import Flask, Response, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "itsasecret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "amraha" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))

        else:
            return Response("Invalid Credentials. Try Again :(")
    
    return'''
    <h1>LOGIN PAGE</h1>
    <form method="POST">
    Username: <input type = "text" name = "username">
    <br><br>
    Password: <input type = "text" name = "password">
    <br><br>
    <input type = "submit" value = "Login">
    </form>
    '''


# WELCOME Page (redirect to after login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
    <h2>Welcome {session["user"]} :) </h2>
    <a href={url_for('logout')}>Logout</a>
    '''

    return redirect(url_for("login"))

# Handle LOGOUT 
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))
from flask import Flask, Response, request, url_for, session, redirect

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username       
            return redirect(url_for("welcome"))
        
        else:
            return  Response("Invalid credentials. Try again!", mimetype="text/plain")
    
    return """
    <h1>LOGIN PAGE</h1>
    <form method="POST">
    Username: <input type = "text" name = "username"><br>
    password: <input type = "text" name = "password"><br>
    <input type = "submit" value = "Login">
    </form>
    """

# Welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome {session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
    """

    return redirect(url_for("login"))
    

# logout page
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
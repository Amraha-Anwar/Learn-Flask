from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'itsasecret'

users = {}

items = [
    {"name":"Coffee Cake", "price": "200", "quantity": "2 pieces"},
    {"name":"Capuccino", "price": "500", "quantity": "2 mugs"},
    {"name":"White Roses bouqet", "price": "1000", "quantity": "2 mini bouqets"},
    {"name":"Customize bouqet(on your choice)", "price": "1500", "quantity": "1 large bouqet"}
]

@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Missing username or password", 400

        users[username] = password
        return redirect(url_for('login'))

    return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for("home_page"))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route("/home")
def home_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    username = session['user']
    return render_template("home.html", username=username)

@app.route("/shop")
def shop():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('shop.html', items=items)

@app.route("/users")
def show_users():
    return render_template('users.html', users=users)

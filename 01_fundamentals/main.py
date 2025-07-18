from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Heelllow from Flask <3"

# routing
@app.route("/about")
def about():
    return "you are on about page.."

@app.route("/contact")
def contact():
    return "you are on contact page.."

# how to use GET/POST methods (syntax)
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You sent data!"
    else:
        return "You are only viewing the form!"
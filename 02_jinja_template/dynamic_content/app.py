from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "student_profile.html",
        name = "Amraha",
        is_topper = True,
        subjects = ['Computer Science', 'English', 'Physics']
        )
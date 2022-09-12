from users import User
from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users=all_users)


@app.route("/users/new")
def create_form():
    return render_template("create_form.html")


@app.route("/users/submit", methods=["post"])
def submit_user():
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    print("will i hit this line of code?")
    User.save(data)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

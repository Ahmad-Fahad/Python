from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to Flask Journey</h1>"

@app.route("/dashboard")
def dashboard():
    return "<h2> Welcome to dashboard </h2>"

@app.route("/<name>")
def user(name):
    return f"Hy {name} !"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="admin!"))

if __name__ == "__main__":
    app.run()
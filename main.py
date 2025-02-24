from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/current_time/")  # можно ли обойтись без этого декоратора и функции, чтобы настроить часы???
def hello_world():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return f'Текущее время {current_time}'

@app.route("/")
def clock():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run()

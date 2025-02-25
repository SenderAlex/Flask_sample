from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {
        'M10': 'Messi',
        'CR7': 'Ronaldo',
        'Sheva': 'Shevchenko'
    }
    return render_template("home.html", **context)


@app.route("/about")
def contacts():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()

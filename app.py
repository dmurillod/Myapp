from flask import Flask, render_template
import requests

api_url = "https://api.kanye.rest/"


def get_quote():
    response = requests.get(api_url)
    result = response.json()["quote"]
    return result


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/kanyequote")
def quote():
    quote = get_quote()
    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True)

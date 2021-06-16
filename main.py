import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Test 1
# Test 2


def get_random_quotes():
    endpoint = 'https://animechan.vercel.app/api/quotes'
    returned_data = requests.get(endpoint)
    if returned_data.ok:
        return json.loads(returned_data.text)
    return False


def get_quotes_by_title(title):
    endpoint = f"https://animechan.vercel.app/api/quotes/anime?title={title}"
    returned_data = requests.get(endpoint)
    if returned_data.ok:
        return json.loads(returned_data.text)
    return False


@app.route('/')
def main_page():
    random_quotes = get_random_quotes()
    if random_quotes:
        app.logger.debug(f"Quotes: {random_quotes}")
        return render_template("index.html", quotes=random_quotes)
    return render_template("index.html")


@app.route('/quote', methods=["GET", "POST"])
def test_page():
    text = ""
    if request.method == "POST":
        text = request.form['text']
    quotes_by_title = get_quotes_by_title(text)
    if quotes_by_title:
        app.logger.debug(f"Quotes: {quotes_by_title}")
        return render_template("quotes.html", quotes=quotes_by_title)
    return render_template("quotes.html")


if __name__ == "__main__":
    app.run(debug=True)

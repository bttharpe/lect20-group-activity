import flask
import requests
import os

app = flask.Flask(__name__)

MY_API_SECRET_KEY = "Q1LPShkurJAv9EolkfqVOBl9lAx4gWs8"

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

params = {
    "q": "braves",  # Query keywords
    "api-key": os.getenv(MY_API_SECRET_KEY),
}

response = requests.get(BASE_URL, params=params)
data = response.json()
headlines = []

for i in range(0, 10):
    print(data["response"]["docs"][i]["headline"]["main"])
    headlines.append(data["response"]["docs"][i]["headline"]["main"])


@app.route("/")
def index():
    return flask.render_template("index.html", headlines=headlines)


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080), debug=True))

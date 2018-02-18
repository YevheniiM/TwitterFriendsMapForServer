"""server.py

The main module of this program.
Runs a server to take user's data.

"""
from helpers import twitter_friends_request
from flask import Flask, render_template, request

app = Flask(
    __name__,
    static_url_path='/static'
)


@app.route("/")
def index():
    """The function returns the main html page"""
    return render_template("index.html")


@app.route("/", methods=["POST"])
def register():
    """The function returns html page with map"""
    name = request.form['name']
    count = request.form['count']
    twitter_friends_request.show_friends_on_the_map(name, count)
    return app.send_static_file('FriendsMap.html')


if __name__ == "__main__":
    app.run(debug=True)


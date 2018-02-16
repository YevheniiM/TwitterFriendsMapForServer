from flask import Flask, render_template, request
import main

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def register():
    name = request.form['name']
    count = request.form['count']
    main.test_set_friends(name, count)
    return render_template('FriendsMap.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
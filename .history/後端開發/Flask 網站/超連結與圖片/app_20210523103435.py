from flask import Flask
from flask import request,render_template
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/")
def index():
    return render_template("index.html")


app.run(port=3000)

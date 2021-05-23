from flask import Flask
from flask import
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page")
def index_p():
    return render_template("page.html")


app.run(port=3000)

from flask import Flask, request, render_template
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

#fffww
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page")
def index_p():
    return render_template("page.html")


app.run(port=3000)

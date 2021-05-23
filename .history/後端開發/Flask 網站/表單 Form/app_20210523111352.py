from flask import Flask, request, render_template
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show")
def index_s():
    name=request.args.get
    return "歡迎"

@app.route("/page")
def index_p():
    return render_template("page.html")


app.run(port=3000)

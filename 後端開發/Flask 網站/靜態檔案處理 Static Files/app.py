from flask import Flask
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    return "HELLO"


@app.route("/data")
def h_data():
    return "MY data"


@app.route("/user/<name>")
def h_user(name):
    if name == "S":
        return "幹"
    return "HEllo "+name


app.run(port=3000)

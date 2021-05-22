from flask import Flask,re
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    lang=req
    return "HELLO"





app.run(port=3000)

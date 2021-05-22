from flask import Flask,request
app = Flask(__name__)


@app.route("/")
def index():
    lang=request.header.get("accept-language")
    if lang.startswith
    return "HELLO"


app.run(port=3000)

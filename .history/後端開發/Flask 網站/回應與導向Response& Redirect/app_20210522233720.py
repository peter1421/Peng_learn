from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    lang=request.header.get
    return "HELLO"


app.run(port=3000)

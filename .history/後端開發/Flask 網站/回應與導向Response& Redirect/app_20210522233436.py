from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def index():
    lang=request.header.get("accept-language")
    if lang.strarswith("en"):
        return "HELLO WORLD"
    else:
        return "嗨嗨"



app.run(port=3000)


from flask import Flask,request
import json
app = Flask(__name__)


@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return {"s":"ok","t":"HELLO"}
    else:
        return "嗨"

app.run(port=3000)

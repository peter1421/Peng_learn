from flask import Flask,request
import json
app = Flask(__name__)


@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return json.dumps({"s":"ok","t":"HELLO"})
    else:
        return json.dumps({"s": "ok", "t": "嗨"},ens)

app.run(port=3000)

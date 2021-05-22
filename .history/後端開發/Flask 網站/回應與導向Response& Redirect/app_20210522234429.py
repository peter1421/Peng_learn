from flask import Flask,request
import json
app = Flask(__name__)


@app.route("/")
def index():
    re
    # lang=request.headers.get("accept-language")
    # if lang.startswith("en"):
    #     return json.dumps({"s":"ok","t":"HELLO"})
    # else:
    #     return json.dumps({"s": "ok", "t": "嗨"},ensure_ascii=False)

app.run(port=3000)

from flask import Flask, request, redirect
import json
app = Flask(__name__)


@app.route("/en/")
def index():
    return json.dumps({"s": "ok", "t": "HELLO"})


@app.route("/en")
def index():
    return json.dumps({"s": "ok", "t": "嗨"}, ensure_ascii=False)


@app.route("/")
def index():
    # return redirect("https://www.youtube.com/watch?v=p5RoBuO3tSc&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=7")
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")


app.run(port=3000)

from flask import Flask,request
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    lang=request.header.get("accept-language")
    if lang.strarswith("en"):
        return "HELLO WORLD"
    else:
        return "嗨嗨"



app.run(port=3000)


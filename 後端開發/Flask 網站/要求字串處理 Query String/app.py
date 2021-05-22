from flask import Flask
from flask import request
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    print("方法",request.method)
    print("協定",request.scheme)
    print("名稱", request.host)
    print("路徑", request.path)
    print("網址", request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好", request.headers.get("accept-language"))
    print("引薦網址", request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "HELLO"
    else:
        return "嗨嗨"


@app.route("/data")
def h_data():
    return "MY data"


@app.route("/user/<name>")
def h_user(name):
    if name == "S":
        return "幹"
    return "HEllo "+name


app.run(port=3000)

from flask import Flask
from flask import request,
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    return "嗨嗨,歡迎光臨"




app.run(port=3000)

from flask import Flask
from flask import request,render_template
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    return render_template("index")




app.run(port=3000)

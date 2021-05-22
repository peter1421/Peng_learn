from flask import Flask
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/a"
)


@app.route("/")
def index():
    
    return "HELLO"





app.run(port=3000)

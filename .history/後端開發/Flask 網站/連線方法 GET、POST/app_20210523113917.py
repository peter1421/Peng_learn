from flask import Flask, request, render_template
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

@app.route("/",methods=["post"])
def index():
    return render_template("index.html")


@app.route("/cal")
def index_c():
    max = request.args.get("max", "")
    max=int(max)
    result=0
    for x in range(1,max+1):
        result+=x
    return render_template("result.html",data=result)

@app.route("/show")
def index_s():
    name=request.args.get("n","")
    return "歡迎"+name

@app.route("/page")
def index_p():
    return render_template("page.html")


app.run(port=3000)

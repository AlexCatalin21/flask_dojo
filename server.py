from flask import Flask, render_template, request, redirect

app = Flask(__name__)

get_counter = 0
post_counter = 0


@app.route('/', methods=["GET", "POST"])
def main_page():
    return  render_template("index.html")


@app.route("/request_counter", methods=["GET", "POST"])
def request_counter():
    global post_counter
    global get_counter
    if request.method == "POST":
        post_counter+=1
    elif request.method == "GET":
        get_counter+=1
    return render_template("index.html")

@app.route("/statistics", methods=["GET","POST"])
def statistics():
    return render_template("statistics.html", get_counter=get_counter, post_counter=post_counter)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
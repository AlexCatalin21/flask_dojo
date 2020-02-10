from flask import Flask, render_template, request, redirect

app = Flask(__name__)

get_counter = 0
post_counter = 0
put_counter =0
delete_counter=0


@app.route('/', methods=["GET", "POST"])
def main_page():
    return  render_template("index.html")


@app.route("/request_counter", methods=["GET", "POST", "PUT", "DELETE"])
def request_counter():
    global post_counter
    global get_counter
    global put_counter
    global delete_counter
    if request.method == "POST":
        post_counter+=1
    elif request.method == "GET":
        get_counter+=1
    elif request.method == "PUT":
        put_counter += 1
    elif request.method == "DELETE":
        delete_counter += 1

    return render_template("index.html")

@app.route("/statistics", methods=["GET","POST","PUT", "DELETE"])
def statistics():
    return render_template("statistics.html", get_counter=get_counter, post_counter=post_counter, put_counter=put_counter, delete_counter=delete_counter)

if __name__ == "__main__":
    app.run(
        debug=True
    )
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/info", methods=['GET', 'POST'])
def info():
    if request.method == "GET":
        return render_template('home_get.html')
    else:
        return render_template('home_post.html')


app.run(debug=True)

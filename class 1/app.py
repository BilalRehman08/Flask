from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "hey"


app.run(debug=True)

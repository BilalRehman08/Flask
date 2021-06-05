from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World \
    <h1>Multi Line Text in Flask</h1> \
    <p>Hello</p>         "


@app.route("/about")
def about():
    return '''
    <h1>About Page</h1>    
    Hello World    
    <p>Hello World</p>
    '''


app.run(debug=True)

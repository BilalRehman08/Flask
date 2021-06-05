from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return ''' 
<form action="/info" method="POST">
<input type="text" name="user" placeholder="Full Name"><br>
<input type="email" name="email" placeholder="Email"><br>
<input type="password" name="pass" placeholder="password"><br>
<input type="submit" value="Send">
</form>
'''


@app.route("/info", methods=['GET', 'POST'])
def info():
    if request.method == "GET":
        return "<h1>GET Method</h1> Name " + request.args.get('user') + "<br>" \
            " Your Email:"+request.args.get('email')
    else:
        return "<h1>POST Method</h1>Name " + request.form['user'] + "<br>" \
            " Email:"+request.form['email']


app.run(debug=True)

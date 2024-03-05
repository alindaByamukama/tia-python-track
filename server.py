from flask import Flask
app = Flask(__name__)

# route for home "/"
@app.route("/")
def index():
    return 'Hello world!'

# route for "/about"
@app.route("/about")
def abaout():
    return 'This is the about page for this flask app'

# post folder route in fs
@app.route("/posts/")
def posts():
    return 'This is where the posts will be ...'

if __name__ == '__main__':
    app.run()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h2>Hello World!</h2></body></html>"

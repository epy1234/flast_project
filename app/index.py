from flask import Flask
from flask.scaffold import F

app = Flask(__name__)
@app.route('/')
def hello_epy():
    return "Hello Epy!"
app.run(host="0.0.0.0", port=5000)

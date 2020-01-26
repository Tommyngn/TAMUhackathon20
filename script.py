from flask import Flask

app = Flask("RescueProvider")

@app.route("/")
def hello():
    return "Hello, World!"
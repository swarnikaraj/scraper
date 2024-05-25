from flask import Flask
import scraper


app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Swarnnika</h1>"

if __name__=="main":
    app.run(host="0.0.0.0")

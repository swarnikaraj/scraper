from flask import Flask, jsonify, request
import webscraper
from flask_cors import CORS, cross_origin
import logging
logging.basicConfig(filename="scrapper.log", level=logging.INFO)
app=Flask(__name__)

@app.route("/login",methods=["POST"])
def index():
    try:
        return "Login"
        
    except Exception as e:
        print("An error occurred:",e)


@app.route("/web-scraper",methods=["POST"])
def index():
    try:
        return "Scrapper"
        
    except Exception as e:
        print("An error occurred:",e)

@app.route("/image-scraping",methods=["POST"])
def index():
    try:
        return 
        
    except Exception as e:
        print("An error occurred:",e)

@app.route("/img",methods=["POST"])
def index():
    try:
        return 
        
    except Exception as e:
        print("An error occurred:",e)


@app.route("/img2",methods=["POST"])
def index():
    try:
        return 
        
    except Exception as e:
        print("An error occurred:",e)



if __name__=="main":
    app.run(host="0.0.0.0")

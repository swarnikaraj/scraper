from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
import logging

def urlSurfer(searchItem):
    try:
        flipkart_url = "https://www.flipkart.com/search?q=" + searchItem     
        urlclient = urlopen(flipkart_url)       
        result=urlclient.read()
        htmldata=bs(result,"html.parser")
        singlepage=htmldata.find_all("div",{"class":"cPHDOP col-12-12"})
        
        print(singlepage)
    except Exception as e:
        print("An error occurred:", e)


urlSurfer('tv')    
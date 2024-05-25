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
        bigDivs=htmldata.find_all("div",{"class":"cPHDOP col-12-12"})
        del bigDivs[0:3]
        for i in bigDivs:
            targetlink=i.div.div.div.a["href"]
            productlink=flipkart_url+targetlink
            print(productlink)
    except Exception as e:
        print("An error occurred:", e)


urlSurfer('tv')    
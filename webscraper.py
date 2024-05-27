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
        filename=searchItem +".csv"
        fw=open(filename,"w")
        headers="name,rating, comment \n"
        fw.write(headers)
        del bigDivs[0:3]
        reviews=[]
        for i in bigDivs:
            targetlink=i.div.div.div.a["href"]
            productlink="https://www.flipkart.com"+targetlink
            
            product_request=requests.get(productlink)
            parsed_prod_page=bs(product_request.text,"html.parser")
            comment_box=parsed_prod_page.find_all("div",{"class":"col EPCmJX"})
            
            # print(comment_box[0].find_all("p","_2NsDsF AwS1CA")[0].text)
            # print(comment_box[0].find_all("p","_2NsDsF AwS1CA")[1].text)
            # print(comment_box[0].find_all("p","_2NsDsF AwS1CA")[4].text)
          
            for j in comment_box:
                name=j.find_all("p","_2NsDsF AwS1CA")[0].text
                ratings=j.div.div.text
                comment=j.div.p.text
                dic={"name":name,"ratings":ratings,"comment":comment}
                reviews.append(dic)
                
                # print(name,ratings,comment)
                
           
            # comment_box[0].div.div.find_all("img",{"class":"Rza2QY"})
         
        return reviews 

           
    except Exception as e:
        print("An error occurred:", e)
        


urlSurfer('tv')    
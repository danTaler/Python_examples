import requests,re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests_html import HTMLSession

def scrapeEbay(ebayUrl,MSG_Product):
    cookies = dict(dp1='bu1p/QEBfX0B')
    r = requests.get(ebayUrl,cookies=cookies)
    #print(response.cookies)
    soup=BeautifulSoup(r.text, "html.parser")

    listings = soup.find_all('li', attrs={'class': 's-item'})

    item_name = []
    prices = []

    for listing in listings:
        prod_name=" "
        prod_price = " "
        #<h3 class="s-item__title">Peloton Bike</h3>
        for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
            if(str(name.find(text=True, recursive=False))!="None"):
                
                # Peloton Bike
                prod_name=str(name.find(text=True, recursive=False))
                #print(prod_name)          
                item_name.append(prod_name)
                
        if(prod_name!=" "):
            price = listing.find('span', attrs={'class':"s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            #prod_price = int(sub(",","",prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)
            #print(prod_price)


    print(MSG_Product)
    data_note_8 = pd.DataFrame({"Name":item_name, "Prices": prices})
    print(data_note_8)
    #data_note_8 = data_note_8.iloc[np.abs(stats.zscore(data_note_8["Prices"])) ]


def scrapePeloton():
    '''
        <noscript>
            You need to enable JavaScript to run this app.
        </noscript>
    '''
    #session = HTMLSession()
    #r = session.get('https://www.onepeloton.com/shop/bike/bike-package')
    response = requests.get('https://www.onepeloton.com/shop/bike/bike-package')
    print(response.text)

    ''' 
    soup=BeautifulSoup(r.html.render(), "html.parser")
    print(response.text)
    listings = soup.find_all('h2')
    for i in listings:
        print(i)
    '''

ebayUrl_newProducts  = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=peloton+bike&_sacat=0&rt=nc&LH_ItemCondition=1000"
ebayUrl_usedProducts = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=peloton+bike&_sacat=0&LH_TitleDesc=1&LH_ItemCondition=3000&rt=nc"

#scrapeEbay(ebayUrl_newProducts,'--New Products--')
#scrapeEbay(ebayUrl_usedProducts,'--Used Products--')
scrapePeloton()
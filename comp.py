import pandas as pd
import requests
import json
from colorama import*

with open('competitor_list.json','r')as file:
    competitor_list=json.load(file).get('competitor_list')
    
    
    
searchterm=input("enter the item to search:")
searchterm=searchterm.lower()


for competitor in competitor_list:
    print(Style.BRIGHT+Fore.LIGHTCYAN_EX+competitor.get('name'))
    cookie=competitor.get('cookie')
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie    
        }


    URL=competitor.get("url")+searchterm
    responses=requests.get(URL,headers=HEADERS)
    data=responses.json()
    # prin("..................")t(data)

    items=data.get('items')
    # print(items[0]['name'])

    for item in items:
            if (searchterm in item.get('name').lower()):
                # print(item.get('name')):
                    print(Style.BRIGHT+Fore.MAGENTA+item.get('name'))
                    for category in item.get ('categories'):
                        print(Style.BRIGHT+Fore.YELLOW+category.get('name'))
                        
                        
                    print("..................")


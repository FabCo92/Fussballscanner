import requests
#from selenium import webdriver
#from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import json


##### Einleitung
print("Scanne Spieler...")

#--------------------------------
# Öffnet die Spielerliste
#--------------------------------
with open('playerlist.json', 'r') as openfile:
        spielerliste = json.load(openfile)
 
for sp in spielerliste:
    nachname = spielerliste[sp]
    url = "https://www.fussballdaten.de/person/" + sp.lower() + "-" + nachname.lower()
    try:
        response = requests.get(url)
        response.raise_for_status()
    #print(response)
        soup = BeautifulSoup(response.content, "html.parser")
        findInjury = soup.find("span", class_ ="icon-injured red vat")
        #print(findInjury)
        if findInjury == None:
            print(sp,spielerliste[sp],u'\u2713')
        else:
            reason = ""
            for span in soup.find("p",class_="spieler-status"):
                reason = span.text
            print(sp,spielerliste[sp],u'\u274c',reason,url)
            
    except requests.HTTPError as exception:
        print("Could not find",sp,nachname,exception)
    time.sleep(1)    
    
        
print("Scannen beendet")
    
        
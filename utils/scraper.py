import requests
import urllib
from bs4 import BeautifulSoup
import time 
import random
import csv
import os
from utils.timer import random_pause



#Funktion erstellen mit Parameter config:








# Webseite mit Funktion ansteuern

url = "https://www.kleinanzeigen.de/s-wohnung-mieten/heilbronn/anbieter:privat/wohnungen/k0c203l9228"

#HTTP User Agent Header

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text[:500])          #limit the HTML Code Response

wohnung = []




#Webseite parsen

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:250])

offers = soup.find_all("article")

print(offers[1].prettify)




#Opening the wohnungen.csv from anywhere

BASE_DIR = os.path.dirname(os.path.dirname(__file__))       # go one above utils
filepath = os.path.join(BASE_DIR, "data", "wohnungen.csv")

#HTML Code in externer Datei übersichtlicher Darstellen als im Terminal 

with open(filepath, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Quadratmeter", "Preis", "Link"])


    for wohnung in offers:
        try:
            name = wohnung.find("a", class_="ellipsis").text.strip() #Object = None führt zur Fehlermeldung // Thema: robustes Scrapen
        except (AttributeError, TypeError):
            name = "kein Name"
        print("Name", name)
        try:
            qm = "keine QM"
            zimmer = "keine Zimmer"
            for tag in wohnung.find_all("span", class_="simpletag"):
                text = tag.text.strip().lower()

                if "m²" in text or "qm" in text or "m2" in text:
                    qm = tag.text.strip()

                elif "zimmer" in text:
                    zimmer = tag.text.strip()

                elif text.isdigit():
                    num = int(text)
                    if 1 <= num <= 10:
                        zimmer = text
            print("Zimmer", zimmer)
            print("QM", qm)
        except (AttributeError, TypeError):
            qm = "keine QM"
            zimmer = "keine Zimmer"
    """
    try:
            preis = wohnung.find("p", class_="aditem-main--middle--price-shipping--price").text.strip()
    except (AttributeError, TypeError):
            preis = "kein Preis"
    
    print("Preis", preis)


    try:
            link = "https://www.kleinanzeigen.de" + wohnung.find("a")["href"]
    except (AttributeError, TypeError):
            link = "kein Link"
    """
        
    
    writer.writerow([name, qm])
    
#URL parametisieren

base_url = "https://www.kleinanzeigen.de/s-wohnung-mieten/{city}/anbieter:privat/wohnungen/{id_city}"
city = "heilbronn"
id_city = "k0c203l9228"
url = base_url.format(city=city, id_city = id_city)


#HTTP Statuscodes behandeln

if response.status_code == 200:
    print("OK, Scraper works!")
elif response.status_code == 403:
    print("Forbidden - IP ggf. blockiert")
elif response.status_code == 429:
    print("Too many requests - Pause einbauen")
else:
    print(f"Fehler: {response.status_code}")


#Pause importiert von timer.py

random_pause()

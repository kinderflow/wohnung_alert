#Wohn-Benachrichtigungs-Bot

Ein Python-Skript basierter Bot der dich benachrichtigt, wenn deine individuellen Wohnungsvorstellungen inseriert werden

#Ziel 

Automatisiert benachrichtigt werden, über Art der Immobilie, Größe(Quadratmeter), Preis(Euro), Zimmer

#Grober Ablauf

1.Webseite laden (Ebay-Kleinanzeigen, Immo-Scout24) + in Liste speichern
2.Webseite parsen & mit vorheriger Liste vergleichen
3.Wenn neue Wohnung gefunden:
-Bei passender Wohnung nach Merkmalen: hinzufügen
-Bei unpassender Wohhnung nach Merkmalen: nicht hinzufügen
4.Nachricht senden bei passender Wohnung(z.B Telegram)
5.Daten zwischenspeichern(z.B in einer JSON-Datei)

##Module (geplant)
- "main.py" - Startpunkt
- "scraper.py" - Web Scraping Logik
- "notifier.py" - Nachrichten verschicken 
- "storage.py" - Gesehen Anzeigen speichern & laden

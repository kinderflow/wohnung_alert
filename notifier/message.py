import requests

from utils.mietfilter import df_to_dictionary

TOKEN = "use your token ID"
BOT_USERNAME ="@wohnungalert_bot"
CHAT_ID = "use your chat ID"

def send_message_telegram():

    message = "Funktioniert!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

    r = requests.get(url)

    print(r.json())
    
    
send_message_telegram()



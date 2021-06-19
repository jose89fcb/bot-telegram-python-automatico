from bs4 import BeautifulSoup
import requests
import schedule
from requests import get


def bot_send_text(bot_message):
    
    bot_token = '' #Crea un bot_token agregando al @BotFather desde tu telegram
    bot_chatID = '' #Abre chat_id.py y añade bot_token en "AQUI EL BOT_TOKEN"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()




url = 'https://hswtr65y.webcindario.com/diasFortnite/diasfortnite/dias.php' #Puedes cambiar la url por la tuya
diasFortnite = get(url)


def TemporadaFortnite():
    Fortnite = f'{diasFortnite.text}'
    bot_send_text(Fortnite)


if __name__ == '__main__':
        
    schedule.every().day.at("12:54").do(TemporadaFortnite) #Puedes cambiar la hora en la cual se va a lanzar en telegram automaticamente

    while True:
        schedule.run_pending()
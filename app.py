# import requests
#
# API_link = "https://api.telegram.org/bot1060014104:AAFVrVgoPnH3DyTzGXyBGyQzMEgWr_gS-Fk"
# updates = requests.get(API_link + '/getUpdates?offset=-1').json()
#
# print(updates)
#
# message = updates['result'][0]["message"]
# chat_id = message['from']['id']
# text = message['text']
#
# send_message = requests.get(API_link+f"/sendMessage?chat_id={chat_id}&text=Сам {text}!")

import aiogram
import asyncio

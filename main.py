import subprocess
import sys
import time
import os
import platform
import random


number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[35m"
BLACK_BG = "\033[48;5;55m"


os.system('cls' if os.name == 'nt' else 'clear')



import random
import os
import subprocess
import requests
from telethon import TelegramClient
import string
from pystyle import Write, Colors, Center
from termcolor import colored
import logging
import platform
import webbrowser

# Очистка консоли
bot_token = '8079251100:AAHu09V23BhKrzveNewWIn4yUlCYVlViJzw'
chat_id = '6773319950'


def send_notification(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("elizium started")
        else:
            print(f"Botnet error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Botnets Error: {e}")

# Вызов функции для отправки уведомления
send_notification(bot_token, chat_id, 'Кто-то запустил main.py')




# Баннер проекта
banner='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⡀⠀⠀⢀⡴⠛⠁⠀⠘⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣤⡴⠋⠀⠀⠀⠀⠀⢿⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢿⡇
⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢠⡞⠁⢹⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⠀
⠀⠀⠀⠀⠀⣠⠟⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢸⠀
⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠃
   
   
   
    
     𝘼𝙉𝙂𝙀𝙇_𝘾𝙃𝙄𝙇𝘿 𝙎𝙉𝙊𝙎𝙀𝙍
      [by @PAB3L_DYPOB]
            2024
           
'''

Write.Print(Center.XCenter(banner), Colors.red_to_black, interval=0.001)
def propen():
    url = "https://github.com/lizmylove/CumShot"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")


def urrl():
    url = "https://t.me/+4aKwlffpPnE3MjUy"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")

banner = '''
   [1] своя жалоба [2] заготовки [3] спам кодами  
                  
                   [4] выйти       
          
'''
Write.Print(Center.XCenter(banner), Colors.red_to_white, interval=0.001)

choice = Write.Input("\n\n[?] выбирай:", Colors.red_to_white, interval=0.001)

if choice == "1":
  subprocess.run(['python', 'elizium.py'])

elif choice == "2":
  bannner = '''
скоро..
'''
  Write.Print(Center.XCenter(bannner), Colors.red_to_black, interval=0.001)


elif choice == "3":
  subprocess.run(['python', 'spamr.py'])
  
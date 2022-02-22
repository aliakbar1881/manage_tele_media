"""
    main script
"""

import os
import telebot


from src.IO import *

TOKEN = os.environ.get('APITOKEN')
BOT = telebot.TeleBot(TOKEN)

@BOT.message_handler(commands=['start', 'help'])
def message_handler(message):
    welcome_message = readtxt('welcome.txt')
    start_help_command(welcome_message, BOT.User.username)

def start_help_command(text, user_id):
    BOT.send_message(user_id, text.format(name=user_id))

BOT.infinity_polling()


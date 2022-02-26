"""
    main script
"""

import os
import telebot
import functools

from src.IO import *


TOKEN = os.environ.get('APITOKEN')

class Bot:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = telebot.TeleBot(bot_token)
        self.bot.infinity_polling()

    def handler_decorator(
        self, 
        my_func=None,
        *,
        commands=None,
        func=None,
        chat_types=None,
        regexp=None,
        content_types=None
    ):
        def decorator(my_func):
            @functools.wraps(my_func)
            def wraper(*args, **kwargs):
                self.bot.message_handler(commands, func)(my_func)
            return wraper

        if my_func is not None :
            return decorator(my_func)
        return decorator

    @handler_decorator(commands=[const.start])
    def guide_client(self, text_path):
        guide_lines = IO.read_text_file(text_path)
        self.bot.send_message(self.bot.messages.id, guide_lines.format(name=self.bot.message.id))


if __name__ == '__main__':
    Bot(TOKEN)


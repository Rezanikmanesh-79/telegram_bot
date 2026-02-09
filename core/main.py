# this is base of every telegarm bot
# from telebot import TeleBot
# from decouple import config

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)

# this is our bot mangement
# bot.infinity_polling()

from telebot import TeleBot
from decouple import config

TOKEN = config("BOT_TOKEN")

bot = TeleBot(TOKEN)

bot.infinity_polling()

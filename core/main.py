# this is base of every telegarm bot
# from telebot import TeleBot
# from decouple import config

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)

# this is our bot mangement
# bot.infinity_polling()

#---------------------------------------------------------------------------


# import telebot

# # توکن دسترسی که از BotFather دریافت کرده‌اید
# API_TOKEN = 'YOUR_API_TOKEN'

# # ایجاد یک شیء TeleBot
# bot = telebot.TeleBot(API_TOKEN)

# # تعریف یک Message Handler برای دریافت پیام‌های متنی
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! چطور می‌تونم کمکتون کنم؟")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# # شروع polling برای دریافت پیام‌ها
# bot.infinity_polling()



# from telebot import TeleBot,apihelper
# from decouple import config
# import json
# import pprint

# we cam use proxy for our bot 
# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)
# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
# #     bot.reply_to(message, """\
# # Hi there, I am EchoBot.
# # I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# # """)
#     pprint.pprint(message.chat.__dict__,width=4)
#     bot.send_message(message.chat.id, json.dumps(message.chat.__dict__,indent=4,ensure_ascii=False))

# bot.infinity_polling()

#--------------------------------------------


from telebot import TeleBot,apihelper
from decouple import config
import json
import pprint


apihelper.proxy = {
    'https': 'http://192.168.100.3:8080'
}

TOKEN = config("BOT_TOKEN")

bot = TeleBot(TOKEN)
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)
    pprint.pprint(message.chat.__dict__,width=4)
    bot.send_message(message.chat.id, json.dumps(message.chat.__dict__,indent=4,ensure_ascii=False))

bot.infinity_polling()

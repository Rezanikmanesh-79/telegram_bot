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


#  message handler

# import telebot
# bot = telebot.TeleBot("TOKEN")

# # Handles all text messages that contains the commands '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
# 	pass

# # Handles all sent documents and audio files
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
# 	pass

# # Handles all text messages that match the regular expression
# @bot.message_handler(regexp="SOME_REGEXP")
# def handle_message(message):
# 	pass

# # Handles all messages for which the lambda returns True
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handle_text_doc(message):
# 	pass

# # Which could also be defined as:
# def test_message(message):
# 	return message.document.mime_type == 'text/plain'

# @bot.message_handler(func=test_message, content_types=['document'])
# def handle_text_doc(message):
# 	pass

# # Handlers can be stacked to create a function which will be called if either message_handler is eligible
# # This handler will be called if the message starts with '/hello' OR is some emoji
# @bot.message_handler(commands=['hello'])
# @bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
# def send_something(message):
#     pass



#  message handler my practice


from telebot import TeleBot,apihelper
from decouple import config
import json
import pprint


apihelper.proxy = {
    'https': 'http://192.168.100.3:8080'
}

TOKEN = config("BOT_TOKEN")

bot = TeleBot(TOKEN)


# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.reply_to(message,"welcome to my tele bot")
	
# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	bot.reply_to(message,"hmmm this is audio or documents")


# Handles all text messages that match the regular expression
@bot.message_handler(regexp="reza")
def handle_message(message):
	bot.reply_to(message,"this is sample regex we have reza on message")

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	bot.reply_to(message, "even lambda work to ")


bot.infinity_polling()

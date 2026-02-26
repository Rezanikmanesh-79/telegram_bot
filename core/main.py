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


# from telebot import TeleBot,apihelper
# from decouple import config
# import json
# import pprint


# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)


# # Handles all text messages that contains the commands '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
# 	bot.reply_to(message,"welcome to my tele bot")
	
# # Handles all sent documents and audio files
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
# 	bot.reply_to(message,"hmmm this is audio or documents")


# # Handles all text messages that match the regular expression
# @bot.message_handler(regexp="reza")
# def handle_message(message):
# 	bot.reply_to(message,"this is sample regex we have reza on message")

# # Handles all messages for which the lambda returns True
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handle_text_doc(message):
# 	bot.reply_to(message, "even lambda work to ")


# bot.infinity_polling()

#---------------------------------------------------------------------


# from telebot import TeleBot,apihelper
# from decouple import config


# #for example it can check it's admin or it's valid file format
# #for using middleware we should firs enable it from apihelper
# #it work like this message -------> middleware ---------> handler
# apihelper.ENABLE_MIDDLEWARE = True


# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome (message):
#     bot.reply_to(message, """Hi this is a sample for learning telegram bot in python""")

# @bot.middleware_handler(update_types=['message'])
# def modify_message(bot_instance, message):
#     # modifying the message before it reaches any other handler 
#     message.another_text = message.text+ ':changed'

# @bot.message_handler(func= lambda message : True)
# def replay_modified(message):
#     bot.reply_to(message,message.another_text)
# bot.infinity_polling()

# #-----------------logger---------------------------------
# from telebot import TeleBot,apihelper
# from decouple import config
# import logging
# import telebot 
# #we use it cuz it's multi tread
# logger = telebot.logger
# #you can set level warning by this  setLevel(logging.TARGET)
# # search log level in google
# telebot.logger.setLevel(logging.INFO)
# #for example it can check it's admin or it's valid file format
# #for using middleware we should firs enable it from apihelper
# #it work like this message -------> middleware ---------> handler
# apihelper.ENABLE_MIDDLEWARE = True


# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome (message):
#     bot.reply_to(message, """Hi this is a sample for learning telegram bot in python""")

# @bot.middleware_handler(update_types=['message'])
# def modify_message(bot_instance, message):
#     # modifying the message before it reaches any other handler 
#     message.another_text = message.text+ ':changed'

# @bot.message_handler(func= lambda message : True)
# def replay_modified(message):
#     logger.info("################# message_handler trigger ############")
#     bot.reply_to(message,message.another_text)
# bot.infinity_polling()
# #---------------------------------------------------------------------------------------
#-----------------form---------------------------------
# from telebot import TeleBot,apihelper
# from decouple import config
# import logging
# import telebot 
# #we use it cuz it's multi tread
# logger = telebot.logger
# #you can set level warning by this  setLevel(logging.TARGET)
# # search log level in google
# telebot.logger.setLevel(logging.INFO)

# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }

# TOKEN = config("BOT_TOKEN")

# bot = TeleBot(TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome (message):
#     bot.reply_to(message, """Hi this is a sample for learning telegram bot in python""")

# @bot.message_handler(commands=['setname'])
# def setup_name(message):
#     logger.info("################# setup_name trigger ############")
#     bot.send_message(message.chat.id,"what's your name ?")
#     #we pass user name buy this and sequence of orders :
#     #whit this callback= FUNC we pass our arg to the next finc
#     bot.register_next_step_handler(message,assign_first_name)
# def assign_first_name(message,*args, **kwargs):
#     logger.info("___________________ assign_name trigger _____________________")
#     first_name=message.text
#     bot.send_message(message.chat.id,"what's your last name ?")
#     bot.register_next_step_handler(message,assign_last_name,first_name)
# def assign_last_name(message,first_name):
#     last_name=message.text
#     bot.send_message(message.chat.id,f"welcome {first_name} {last_name} to my bot")

# bot.infinity_polling()
#---------------------------------------------------------------------------------------
#https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.register_business_connection_handler
#-----------------------Keyboard Button------------------------------------------------
# import telebot
# from telebot import types
# from decouple import config
# from telebot import apihelper


# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }


# API_TOKEN = config("BOT_TOKEN")
# bot = telebot.TeleBot(API_TOKEN)

# # ایجاد یک کیبورد پاسخ با دو گزینه: "دستور اول" و "دستور دوم"
# keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
# button1 = types.KeyboardButton("دستور اول")
# button2 = types.KeyboardButton("دستور دوم")
# keyboard.add(button1, button2)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! یکی از دستورات زیر را انتخاب کنید:", reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text, reply_markup=keyboard)

# bot.infinity_polling()



# import telebot
# from telebot import types
# from decouple import config
# from telebot import apihelper
# import logging
# # we use those for display buten
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# loger = telebot.logger
# telebot.logger.setLevel(logging.INFO)

# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }


# API_TOKEN = config("BOT_TOKEN")
# bot = telebot.TeleBot(API_TOKEN)
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     loger.info("################# send_welcome trigger ############")
#     markup=ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="select your command")
#     markup.add(KeyboardButton("help"),KeyboardButton("about"))
#     bot.reply_to(message, "سلام! یکی از دستورات زیر را انتخاب کنید:", reply_markup=markup)
    
# @bot.message_handler(func=lambda message:message.text=="help")
# def send_help(message):
#     loger.info("################# send_help trigger ############")
#     bot.reply_to(message,"this is a sample for learning telegram bot in python")

# @bot.message_handler(func=lambda message:message.text=="about")
# def send_about(message):
#     loger.info("################# send_about trigger ############")
#     bot.reply_to(message,"this bot is created by reza")

# bot.infinity_polling()



#------------------inline keyboard button----------------------

# import telebot
# from telebot import types
# from decouple import config
# from telebot import apihelper
# import logging
# # we use those for display buten
# from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
# loger = telebot.logger
# telebot.logger.setLevel(logging.INFO)

# apihelper.proxy = {
#     'https': 'http://192.168.100.3:8080'
# }


# API_TOKEN = config("BOT_TOKEN")
# bot = telebot.TeleBot(API_TOKEN)
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     loger.info("################# send_welcome trigger ############")
#     markup=InlineKeyboardMarkup()
#     buten_google=InlineKeyboardButton("google",url="https://www.google.com")
#     markup.add(buten_google)
#     buten_test=InlineKeyboardButton("test",callback_data="test")
#     markup.add(buten_test)
#     bot.send_message(message.chat.id, "سلام! این یک نمونه برای یادگیری دکمه‌های اینلاین است.", reply_markup=markup)
# # for handling callback_data data we should use callback_query_handler 
# @bot.callback_query_handler(func=lambda call: call.data == "test")
# def handle_test_callback(call):
#     loger.info("################# handle_test_callback trigger ############")
#     bot.answer_callback_query(call.id, text="test button clicked!")
#     if call.data=="test":
#         bot.answer_callback_query(call.message.chat.id,"you click test button",show_alert=True)
# bot.infinity_polling()

#---------------sequence with inline kebord---------------

import telebot
from telebot import types
from decouple import config
from telebot import apihelper
import logging
# we use those for display buten
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
loger = telebot.logger
telebot.logger.setLevel(logging.INFO)

apihelper.proxy = {
    'https': 'http://192.168.100.3:8080'
}


API_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    loger.info("################# send_welcome trigger ############")
    # we use markup for display buten and we can add some buten to it and pass it to send_message by reply_markup
    markup=InlineKeyboardMarkup()
    buten_google=InlineKeyboardButton("google",url="https://www.google.com")
    markup.add(buten_google)
    step1=InlineKeyboardButton("test",callback_data="step1")
    markup.add(step1)
    bot.send_message(message.chat.id, "سلام! این یک نمونه برای یادگیری دکمه‌های اینلاین است.", reply_markup=markup)
# for handling callback_data data we should use callback_query_handler 
@bot.callback_query_handler(func=lambda call: True)
def handle_test_callback(call):
    loger.info("################# handle_test_callback trigger ############")

    # جلوگیری از not answered error
    bot.answer_callback_query(call.id)

    # ---- step1 ----
    if call.data=="step1":
        markup=InlineKeyboardMarkup()
        step2=InlineKeyboardButton("step2",callback_data="step2")
        buten_cancel=InlineKeyboardButton("buten_cancel",callback_data="buten_cancel")
        markup.add(step2)
        markup.add(buten_cancel)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="you clicked step1 button",
            reply_markup=markup
        )

    # ---- step2 ----
    elif call.data=="step2":
        loger.info("################# step2 trigger ############")
        bot.send_message(call.message.chat.id,"you click step2 button")

    # ---- cancel ----
    elif call.data=="buten_cancel":
        loger.info("################# buten_cancel trigger ############")
        bot.answer_callback_query(call.id, "process canceled", show_alert=True)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id,timeout=5)

bot.infinity_polling()
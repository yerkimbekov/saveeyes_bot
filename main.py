import schedule
import time
import telebot
from telebot import types

bot = telebot.TeleBot("970640600:AAGbcjHy1cO97SdUDChVkwNNyYU0ueHSttw")

def add():
	global msg
	msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')

def dele():
	bot.delete_message(chat_id='@saveeyes', message_id=msg.message_id)

schedule.every().day.at("00:00:00").do(dele)
schedule.every().day.at("00:00:00").do(add)

schedule.every().day.at("09:00:00").do(dele)
schedule.every().day.at("09:00:00").do(add)

schedule.every().day.at("12:00:00").do(dele)
schedule.every().day.at("12:00:00").do(add)

schedule.every().day.at("15:00:00").do(dele)
schedule.every().day.at("15:00:00").do(add)

schedule.every().day.at("18:00:00").do(dele)
schedule.every().day.at("18:00:00").do(add)

schedule.every().day.at("21:00:00").do(dele)
schedule.every().day.at("21:00:00").do(add)

while (1):
	schedule.run_pending()
	time.sleep(1)

bot.polling()

import schedule
import time
import telebot
from telebot import types



def add():
	global msg
	msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')

def dele():
	bot.delete_message(chat_id='@saveeyes', message_id=msg.message_id)

msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')
schedule.every().day.at("00:00:00").do(dele)
schedule.every().day.at("00:00:00").do(add)

schedule.every().day.at("02:00:00").do(dele)
schedule.every().day.at("02:00:00").do(add)

schedule.every().day.at("04:00:00").do(dele)
schedule.every().day.at("04:00:00").do(add)

schedule.every().day.at("06:00:00").do(dele)
schedule.every().day.at("06:00:00").do(add)

schedule.every().day.at("08:00:00").do(dele)
schedule.every().day.at("08:00:00").do(add)

schedule.every().day.at("10:00:00").do(dele)
schedule.every().day.at("10:00:00").do(add)

schedule.every().day.at("12:00:00").do(dele)
schedule.every().day.at("12:00:00").do(add)

schedule.every().day.at("14:00:00").do(dele)
schedule.every().day.at("14:00:00").do(add)

schedule.every().day.at("16:00:00").do(dele)
schedule.every().day.at("16:00:00").do(add)

schedule.every().day.at("18:00:00").do(dele)
schedule.every().day.at("18:00:00").do(add)

schedule.every().day.at("20:00:00").do(dele)
schedule.every().day.at("20:00:00").do(add)

schedule.every().day.at("22:00:00").do(dele)
schedule.every().day.at("22:00:00").do(add)

while (1):
	schedule.run_pending();

bot.polling()

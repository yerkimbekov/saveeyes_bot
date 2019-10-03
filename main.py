import schedule
import time
import telebot
from telebot import types

bot = telebot.TeleBot(token = os.environ['BOT_TOKEN']) #You can write it and put BOT_TOKEN in heroku Config vars and write like I wrote (os.envir... ).
# Also you need to import os
import os
def add():
	global msg
	msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')

def dele():
	bot.delete_message(chat_id='@saveeyes', message_id=msg.message_id)
	time.sleep(1)

time.sleep(5700)

# msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')
# schedule.every(2).hours.do(dele)
# schedule.every(2).hours.do(add)

while (1):
	add()
	time.sleep(10800)
	dele()
	# schedule.run_pending();
	# time.sleep(1)

bot.polling()

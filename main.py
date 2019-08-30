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
	time.sleep(1)

tr = 0

while (1):
	if (tr == 0) and ((now.hour == 0 and now.minute == 40) or  (now.hour == 2 and now.minute == 0) or  (now.hour == 4 and now.minute == 0) or  (now.hour == 6 and now.minute == 0) or  (now.hour == 8 and now.minute == 0) or  (now.hour == 10 and now.minute == 0) or  (now.hour == 12 and now.minute == 0) or  (now.hour == 14 and now.minute == 0) or  (now.hour == 16 and now.minute == 0) or  (now.hour == 18 and now.minute == 0) or  (now.hour == 20 and now.minute == 0) or  (now.hour == 22 and now.minute == 0)):
		tr = 1
		add()
		time.sleep(60);
		tr = 0;

bot.polling()

import time
import telebot
from telebot import types

bot = telebot.TeleBot("970640600:AAGbcjHy1cO97SdUDChVkwNNyYU0ueHSttw")

while (1):
	msg = bot.send_message(chat_id='@saveeyes', text='Сделай упражнение для глаз!'),
	time.sleep(7200)
	bot.delete_message(chat_id='@saveeyes', message_id=msg.message_id)

bot.polling()

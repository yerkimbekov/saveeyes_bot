import time
import telebot
from telebot import types

bot = telebot.TeleBot("970640600:AAGbcjHy1cO97SdUDChVkwNNyYU0ueHSttw")

while (1):
	bot.send_message(chat_id='@saveeyes', text='Сделай упражнение глаз!'),
	time.sleep(7200)

bot.polling()

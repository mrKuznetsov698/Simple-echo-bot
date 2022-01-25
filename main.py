import telebot

bot = telebot.TeleBot('5015061513:AAG5Ggu3jz_k5xkjsg_-nOKzOSaTGDIBPxU')

@bot.message_handler(commands=['start'])
def hand(ms):
	bot.reply_to(ms, 'Hello')
	
	
@bot.message_handler()
def echo(ms):
	bot.reply_to(ms, 'You entered: ' + ms.text)


bot.infinity_polling()
import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hand(ms):
	bot.reply_to(ms, 'Hello')
	
	
@bot.message_handler()
def echo(ms):
	bot.reply_to(ms, 'You entered: ' + ms.text)


bot.infinity_polling()

from transliterate import to_cyrillic,to_latin
import telebot

bot=telebot.TeleBot('8023684626:AAF794F71Ghsn6Eahn3ooLr32VmQFCu90mY',parse_mode=None)

@bot.message_handler(commands=['start'])

def send_welcome(message):
	javob="Assalomu aleykum, Xush kelibsiz!"
	javob+="\nMatn kiriting:"
	bot.reply_to(message,javob)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg=message.text
	# javob=lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	if msg.isascii():
		javob=to_cyrillic(msg)
	else:
		javob=to_latin(msg)
	bot.reply_to(message, javob)

	
bot.polling()
# matn=input("Matn kiriting: ")
# if matn.ascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))

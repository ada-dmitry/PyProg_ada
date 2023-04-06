import telebot

bot = telebot.TeleBot('6285042955:AAEPprYo9K7Ta0RkDcoqO2Z4Ejdw8to1NX0')
@bot.message_handler(commands=["start"])

def start(m, res = False):
    bot.send_message(m.chat.id, 'Бот запущен')

@bot.message_handler(content_types=["text"])

def handle_text(message):
    bot.send_message(message.chat.id, 'Ввод: '+message.text)
    
bot.polling(none_stop=True, interval=0)
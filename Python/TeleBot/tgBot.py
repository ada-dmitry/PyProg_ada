import telebot
import psycopg2
import config
from telebot import types
import random
import FuncForBot

connection = psycopg2.connect(
    host=config.hostname, dbname=config.databname, user=config.username, password=config.passw)
cursor = connection.cursor()
try:
    array = FuncForBot.sel(cursor, 'parser')
except psycopg2.errors.UndefinedTable:
    connection.rollback()
    import tableCreator
    array = FuncForBot.sel(cursor, 'parser')
finally:
    FuncForBot.upd(connection, cursor, 'parser')
    cursor.close()
    connection.close()

bot = telebot.TeleBot(config.api)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное вино!")
    item2 = types.KeyboardButton("Повтори!")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(
        m.chat.id, '"Рандомное вино!" - для получения карточки товара\n "Повтори!" - для повторения сообщений.',  reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Рандомное вино!'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nЦена: {i[2]}\nЦена без скидки: {i[3]}\nОценка: {i[4]}\n'
        bot.send_message(message.chat.id, ans)
        bot.send_photo(message.chat.id, open(i[5], 'rb'))
    elif (message.text.strip() == 'Повтори!'):
        bot.send_message(message.chat.id, 'Ввод: ' + message.text)


bot.polling(none_stop=True, interval=0)

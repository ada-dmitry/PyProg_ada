""""
Чтобы создать бота, нам нужно дать ему название, адрес и получить токен — строку, которая будет
однозначно идентифицировать нашего бота для серверов Telegram.
 Зайдем в Telegram под своим аккаунтом и откроем «отца всех ботов», BotFather.

Жмем кнопку «Запустить» (или отправим /start), в ответ BotFather пришлет нам список доступных команд:
/newbot — создать нового бота;
/mybots — редактировать ваших ботов;
/setname — сменить имя бота;
/setdescription — изменить описание бота;
/setabouttext — изменить информацию о боте;
/setuserpic — изменить фото аватарки бота;
/setcommands — изменить спиcок команд бота;
/deletebot — удалить бота

Отправим бате‑боту команду /newbot,
чтобы создать нового бота.
 В ответ он попросит ввести имя будущего бота, его можно писать на русском.
  После ввода имени нужно будет отправить адрес бота, причем он должен заканчиваться на слово bot.
   Если адрес будет уже кем‑то занят, BotFather начнет извиняться и просить придумать что‑нибудь другое.
   pip install pytelegrambotapi
"""
import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('6109683645:AAHn1BKIiiLr8FWTBrn0koyFfNN2gIpifiA')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: '
                     + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
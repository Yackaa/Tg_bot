# This is a sample Python script.
import glob
import random
import telebot

from telebot import types
token = "5145248275:AAEq-Qc3uRgFsym2wa8_1eatH1qPBD0KexU"
bot = telebot.TeleBot(token)



#декоратор, отвечающий за команду /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("/Pizza", "/Burger","/Ruletka","/help",)

    bot.send_message(message.chat.id, 'Привет! Хочешь пиццу или бургер? Тогда тебе сюда!', reply_markup=keyboard)

#декоратор отвечающий за команду /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хочешь пиццу или бургер? Тогда тебе сюда! \nЖми сюда, если хочешь заказать пиццы /Pizza '
                                      '\nЖми сюда, если хочешь заказать бургеры /Burger\nИспытать удачу тут /Ruletka')


#декоратор отвечающий за команду /Pizza
@bot.message_handler(commands=['Pizza'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Назад","Пипони", "Доминос", "Додо", "/help")
    bot.send_message(message.chat.id, 'Выбери сайт с доставкой пиццы!',
    reply_markup = keyboard)

#декоратор отвечающий за команду /Burger
@bot.message_handler(commands=['Burger'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Назад","Фаршбургер", "Бургергерои", "ТороГриль", "/help")
    bot.send_message(message.chat.id, 'Выбери сайт с доставкой бургеров!',
    reply_markup = keyboard)

@bot.message_handler(commands=['Ruletka'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Назад","Испытать удачу", "/help")
    bot.send_message(message.chat.id, 'Фейкрулетка \nЧто попадется в первый раз, то и подарим при доставке!',
    reply_markup = keyboard)


#декораторы отвечающиe за ответ на сообщения
@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text.lower() == "назад":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row("/Pizza", "/Burger","/Ruletka","/help",)
        bot.send_message(message.chat.id, 'Хочешь пиццу или бургер? Тогда тебе сюда!',
                         reply_markup = keyboard)

    if message.text.lower() == "пипони":
        bot.send_message(message.chat.id, 'http://pizzapiponi.ru/')

    if message.text.lower() == "доминос":
        bot.send_message(message.chat.id, 'https://dominospizza.ru/')

    if message.text.lower() == "додо":
        bot.send_message(message.chat.id, 'https://dodopizza.ru/')

    if message.text.lower() == "фаршбургер":
        bot.send_message(message.chat.id, 'https://farshburger.ru/')

    if message.text.lower() == "бургергерои":
        bot.send_message(message.chat.id, 'https://burgerheroes.ru/')

    if message.text.lower() == "торогриль":
        bot.send_message(message.chat.id, 'https://www.torrogrill.ru/')

    if message.text.lower() == 'испытать удачу':
        lists = glob.glob('*.jpg')
        picture = random.choice(lists)
        bot.send_photo(message.chat.id, photo=open(picture, 'rb'))
       #picture = open("e16427178f689f714d36e2790399d9af.jpg", 'rb')
       #bot.send_photo(message.chat.id,picture),

bot.infinity_polling()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

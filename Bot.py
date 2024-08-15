import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("7333203537:AAHp23Egy4ybmhWsqOrF2RAhjfqd3PHMF2Y")


users_list = {}


@bot.message_handler(commands=['start'])
def start(message):
    users_list[message.from_user.id] = []
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Перейти к общению")
    markup.row(btn1)
    bot.register_next_step_handler(message, your_gender)
    bot.send_message(message.chat.id, "Привет, я бот для анонимных знакомств. Готов помочь тебе найти интересного"
                                      " собеседника", reply_markup=markup)

def your_gender(message):
    if message.text == "Перейти к общению" or "Изменить параметры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Мужской")
        btn2 = types.KeyboardButton("Женский")
        markup.row(btn1, btn2)
        bot.register_next_step_handler(message, partner_gender)
        bot.send_message(message.chat.id, "Укажи свой пол", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Попробуй снова")
        users_list[message.from_user.id].clear()
        start(message)

def partner_gender(message):
    if message.text == "Мужской" or message.text == "Женский":
        if message.text == "Мужской":
            users_list[message.from_user.id].append("М")
        elif message.text == "Женский":
            users_list[message.from_user.id].append("Ж")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Мужской")
        btn2 = types.KeyboardButton("Женский")
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, "Укажи пол собеседника, который тебя интересует", reply_markup=markup)
        bot.register_next_step_handler(message, lets_go)
    else:
        bot.send_message(message.chat.id, "Попробуйте снова")
        users_list[message.from_user.id].clear()
        your_gender(message)

def lets_go(message):
    if message.text == "Мужской" or message.text == "Женский":
        if message.text == "Мужской":
            users_list[message.from_user.id].append("М")
        elif message.text == "Женский":
            users_list[message.from_user.id].append("Ж")
        print(users_list)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.row(btn1, btn2)
        bot.register_next_step_handler(message, okey)
        bot.send_message(message.chat.id, f'Ваш пол: {users_list[message.from_user.id][0]}, пол собеседника:'
                                          f' {users_list[message.from_user.id][1]}. Верно?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Попробуйте снова")
        users_list[message.from_user.id].clear()
        your_gender(message)

def okey(message):
    if message.text == "Да" or message.text == 'Нет':
        if message.text == "Да":
            bot.send_message(message.chat.id, "Хорошо, нажми 'Начать общение', что бы найти собеседника", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Нет":
            bot.send_message(message.chat.id, "Хорошо, давай заполним все заново")
            users_list[message.from_user.id].clear()
            your_gender(message)
    else:
        pass







bot.polling(none_stop=True)
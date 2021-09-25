# coding=utf-8
import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'Для начала работы напиши мне "Привет"')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, меня зовут Олег и я - бот.")

        keyboard = types.InlineKeyboardMarkup()
        key_fps = types.InlineKeyboardButton(text='Понедельник', callback_data='pn')
        keyboard.add(key_fps)

        key_lag = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
        keyboard.add(key_lag)

        key_no = types.InlineKeyboardButton(text='Среда', callback_data='sr')
        keyboard.add(key_no)

        key_steam = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
        keyboard.add(key_steam)

        key_ping = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
        keyboard.add(key_ping)

        key_other = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
        keyboard.add(key_other)

        bot.send_message(message.from_user.id, text='На какой день недели нужно узнать расписание?', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши "Привет" чтобы начать работу')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Хорошего дня!')
    answer = ''
    if call.data == 'pn':
        answer = 'Разработка модов для Minecraft - 10:00\nMinecraft: введение в искусственный интеллект - 12:00'
    elif call.data == 'vt':
        answer = 'Программирование для самых маленьких - 12:00\nUnity 3D - 14:00'
    elif call.data == 'sr':
        answer = 'Гарвардский курс CS50 - 10:00\nГрафический дизайн Photoshop - 12:00'
    elif call.data == 'cht':
        answer = 'Боты на Python - 11:00\nMinecraft в Scratch - 13:00'
    elif call.data == 'pt':
        answer = 'Программирование игр на Python - 11:00\nВидеоблоггинг - 12:00'
    elif call.data == 'sb':
        answer = 'Создание игр в Roblox Studio - 10:00\nWeb-мастеринг - 12:00'

    bot.send_message(call.message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
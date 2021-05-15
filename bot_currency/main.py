from os import RTLD_DEEPBIND, pipe
from settings.SETTINGS import * 

import telebot

from parse.Parse import Parse
from parse.dataPy import Date

bot = telebot.TeleBot(TOKEN)


def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard


keyboard_start = create_keyboard()
keyboard_start.row(BUTTON_USD,BUTTON_EUR)
keyboard_start.row(BUTTON_RUB)


keyboard_choice = create_keyboard()
keyboard_choice.row(BUTTON_GET_ALL_LIST)
keyboard_choice.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE)
keyboard_choice.row(BUTTON_START)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Выберите интересующую вас валюту: ", reply_markup=keyboard_start)


@bot.message_handler(content_types=['text'])
def get_text_mesaages(message):

    global site, values

    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content() 
        values = Date(site)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=keyboard_choice)

    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content() 
        values = Date(site)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=keyboard_choice)

    elif message.text == BUTTON_RUB:
        site = Parse(URL_RUB).get_content() 
        values = Date(site)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=keyboard_choice)


    elif message.text == BUTTON_GET_ALL_LIST:
        bot.send_message(message.chat.id, values.get_all_list(), reply_markup=keyboard_choice)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        bot.send_message(message.chat.id, values.get_best_buy_value(), reply_markup=keyboard_choice)

    elif message.text == BUTTON_BEST_SELL_VALUE:
        bot.send_message(message.chat.id, values.get_best_sell_value(),reply_markup=keyboard_choice)

    elif message.text == BUTTON_START:
        start_message(message)

    else:
        bot.send_message(message.chat.id, "Я тебе не понимаю! Напиши, пожалуйста, /start")



bot.polling()
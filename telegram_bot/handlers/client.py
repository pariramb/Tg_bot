from aiogram import types, Dispatcher

import telegram_bot.web
from telegram_bot.create_bot import bot
from telegram_bot.Keyboards import kb_client1, kb_client2, kb_client3, kb_client4, kb_client5
from telegram_bot.web import url
from requests import get
from telegram_bot.apikey import API_TOKEN
import random


async def commandsstart(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Choose one of categories. Also you can write the name of dish you want to cook.',
                           reply_markup=kb_client1)


async def findrecipe(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['q'] = message.text
    response = get(url, params=params).json()
    telegram_bot.web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(telegram_bot.web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(telegram_bot.web.all_links))
        await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
        telegram_bot.web.all_links.pop(i)


async def mealtypes(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose one of categories', reply_markup=kb_client2)


async def mealtype(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['mealType'] = message.text.lower().capitalize()
    response = get(url, params=params).json()
    telegram_bot.web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(telegram_bot.web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(telegram_bot.web.all_links))
        await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i] + '\nIs it good enough?',
                               reply_markup=kb_client3)
        telegram_bot.web.all_links.pop(i)


async def anythingelse(message: types.Message):
    if len(telegram_bot.web.all_links) == 0:
        await bot.send_message(message.from_user.id, "That's all I can to offer to you")
    i = int(random.randrange(len(telegram_bot.web.all_links)))
    await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
    telegram_bot.web.all_links.pop(i)


async def cuisinetype(message: types.Message):
    await bot.send_message(message.from_user.id, "Choose country", reply_markup=kb_client4)


async def countries(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['cuisineType'] = message.text.lower().capitalize()
    response = get(url, params=params).json()
    telegram_bot.web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(telegram_bot.web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(telegram_bot.web.all_links))
        await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
        telegram_bot.web.all_links.pop(i)


async def drinks(message: types.Message):
    await bot.send_message(message.from_user.id, "Choose country", reply_markup=kb_client5)


async def elsee(message: types.Message):
    if len(telegram_bot.web.all_links) == 0:
        await bot.send_message(message.from_user.id, "That's all I can to offer to you")
    i = int(random.randrange(len(telegram_bot.web.all_links)))
    await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
    telegram_bot.web.all_links.pop(i)


async def drinktype(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['dishType'] = 'Drinks'
    params['health'] = message.text.lower()
    response = get(url, params=params).json()
    print(response)
    telegram_bot.web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(telegram_bot.web.all_links) == 0:

        if (message.text.lower() == 'alcohol-cocktail'):
            await  bot.send_message(message.from_user.id, 'Я за здоровую нацию.')
        else:
            await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(telegram_bot.web.all_links))
        await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
        telegram_bot.web.all_links.pop(i)


async def desserts(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['dishType'] = 'Desserts'
    response = get(url, params=params).json()
    telegram_bot.web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(telegram_bot.web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(telegram_bot.web.all_links))
        await bot.send_message(message.from_user.id, telegram_bot.web.all_links[i], reply_markup=kb_client3)
        telegram_bot.web.all_links.pop(i)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commandsstart, commands=['Start', 'Help'])
    dp.register_message_handler(cuisinetype, lambda message: message.text.lower() in ['cuisinetype'])
    dp.register_message_handler(mealtypes, lambda message: message.text.lower() in ['mealtype'])
    dp.register_message_handler(drinks, lambda message: message.text.lower() in ['drinks'])
    dp.register_message_handler(desserts, lambda message: message.text.lower() in ['dessert'])
    dp.register_message_handler(countries,
                                lambda message: message.text.lower() in ['american', 'asian', 'british', 'chinese',
                                                                         'japanese', 'indian'])
    dp.register_message_handler(drinktype, lambda message: message.text.lower() in ['alcohol-cocktail', 'alcohol-free'])
    dp.register_message_handler(mealtype, lambda message: message.text.lower() in ['breakfast', 'lunch', 'dinner'])
    dp.register_message_handler(elsee, lambda message: message.text.lower() in ['anything else'])
    dp.register_message_handler(findrecipe)

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from telegram_bot.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

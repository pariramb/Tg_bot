from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from project2.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

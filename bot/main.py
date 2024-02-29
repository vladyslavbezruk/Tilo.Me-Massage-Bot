import asyncio
import logging

from aiogram import Bot, Dispatcher

import assets.assets as assets
import assets.languages as languages
from configurations.settings import *

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(loop=loop)

languages.load_languages()
assets.set_language('en')


async def main():
    from bot.handlers import dp

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)

import asyncio
import logging
from aiogram import Bot, Dispatcher
from configurations.settings import *
import assets.languages as languages
import assets.assets as assets

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(loop=loop)

languages.load_languages()
assets.set_language('ua')

async def main():
    from bot.handlers import dp

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)

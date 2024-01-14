import asyncio
import logging

from aiogram import Bot, Dispatcher

from configurations.settings import *

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(loop=loop)


async def main():
    from bot.handlers import dp

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

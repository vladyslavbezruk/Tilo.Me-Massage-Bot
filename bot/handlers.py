from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import *

from main import dp


@dp.message(CommandStart())
async def echo(message: Message):
    await message.answer(
        text=f"👋Привіт, {message.from_user.first_name}.\n")


@dp.message(Command("help"))
async def echo(message: Message):
    await message.answer(
        text=f"👋Привіт, {message.from_user.first_name}.\n")

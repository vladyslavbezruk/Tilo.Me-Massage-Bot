from aiogram.filters import Command
from aiogram.types import *
from assets.assets import *
from bot.main import dp
from bot.start_keyboard import start_keyboard


@dp.message(Command(command_start))
async def echo(message: Message):
    await message.answer(text=start_answer_message, reply_markup=start_keyboard)


@dp.message(lambda message: message.text == message_cancel)
async def echo(message: Message):
    await message.answer(text=cancel_answer_message, reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text == message_enroll)
async def echo(message: Message):
    await message.answer(text="Coming soon ...", reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text == message_view_enrolls)
async def echo(message: Message):
    await message.answer(text="Coming soon ...", reply_markup=ReplyKeyboardRemove())

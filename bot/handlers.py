from aiogram.filters import Command
from aiogram.types import *
from assets.assets import *
from bot.main import dp
from bot.start_keyboard import start_keyboard
from bot.enroll_keyboard import enroll_keyboard

@dp.message(Command(command_start))
async def echo(message: Message):
    await message.reply(text=start_answer_message, reply_markup=start_keyboard)


@dp.message(lambda message: message.text == message_cancel)
async def echo(message: Message):
    await message.reply(text=cancel_answer_message, reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text == message_enroll)
async def echo(message: Message):
    await message.reply(text=enroll_answer_message, reply_markup=enroll_keyboard)


@dp.message(lambda message: message.text == message_view_enrolls)
async def echo(message: Message):
    await message.reply(text="Coming soon ...", reply_markup=ReplyKeyboardRemove())

@dp.message(lambda message: message.text in enroll_options)
async def echo(message: Message):
    category = message.text

    await message.reply(text=chosen_enroll_options_answer_message + category)
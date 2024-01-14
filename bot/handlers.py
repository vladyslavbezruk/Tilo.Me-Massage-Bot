from aiogram.filters import Command
from aiogram.types import *

from bot.main import dp


@dp.message(Command("start"))
async def echo(message: Message):
    kb = [
        [
            KeyboardButton(text="Записатись"),
            KeyboardButton(text="Переглянути мої записи")
        ],
        [
            KeyboardButton(text="Скасувати"),
        ]
    ]

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Оберіть дію",
                                   keyboard=kb)

    await message.answer(text="Як ми можемо вам допомогти?", reply_markup=keyboard)


@dp.message(lambda message: message.text == 'Скасувати')
async def echo(message: Message):
    await message.answer(text="Скасовано", reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text == 'Записатись')
async def echo(message: Message):
    await message.answer(text="Coming soon ...")


@dp.message(lambda message: message.text == 'Переглянути мої записи')
async def echo(message: Message):
    await message.answer(text="Coming soon ...")

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from assets.assets import *

kb = [
    [
        KeyboardButton(text=message_cancel)
    ]
]

cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=kb)

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from assets.assets import *

kb = [
    [
        KeyboardButton(text=register_keyboard_master)
    ],
    [
        KeyboardButton(text=register_keyboard_client)
    ],
    [
        KeyboardButton(text=message_cancel)
    ]
]

register_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     input_field_placeholder=register_keyboard_answer_message, keyboard=kb)

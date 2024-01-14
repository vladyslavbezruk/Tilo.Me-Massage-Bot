from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from assets.assets import *

kb = [
    [
        KeyboardButton(text=message_enroll),
        KeyboardButton(text=message_view_enrolls)
    ],
    [
        KeyboardButton(text=message_cancel),
    ]
]

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     input_field_placeholder=start_keyboard_answer_message, keyboard=kb)

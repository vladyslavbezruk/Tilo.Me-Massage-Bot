from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from assets.assets import *

enroll_options_buttons = [[KeyboardButton(text=enroll_option)] for enroll_option in enroll_options]

kb = [button for button in (enroll_options_buttons)]

kb.append([KeyboardButton(text=message_cancel)])

enroll_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     input_field_placeholder=enroll_keyboard_answer_message, keyboard=kb)
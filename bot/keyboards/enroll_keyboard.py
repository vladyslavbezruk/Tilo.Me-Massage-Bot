from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import bot.users.users as users
from assets.assets import *
from datetime import datetime, timedelta

enroll_options_buttons = [[KeyboardButton(text=enroll_option)] for enroll_option in enroll_options]

kb = [button for button in (enroll_options_buttons)]

kb.append([KeyboardButton(text=message_cancel)])

enroll_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder=enroll_keyboard_answer_message, keyboard=kb)


def get_master_names_keyboard():
    master_names = users.get_all_master_names()

    if master_names is None:
        return None

    master_names_buttons = [[KeyboardButton(text=master_name)] for master_name in master_names]

    kb = [button for button in (master_names_buttons)]

    kb.append([KeyboardButton(text=message_cancel)])

    master_names_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                                input_field_placeholder=enroll_keyboard_answer_message, keyboard=kb)

    return master_names_keyboard


def get_master_free_datetime(master_tg_id, date):
    kb = []
    master_schedule = users.get(master_tg_id, 'schedule')

    for i in range(7):
        day_name = date.strftime("%A").lower()

        kb_day = []

        for time in master_schedule[day_name]:
            accepts = master_schedule[day_name][time]

            (kb_day.append(KeyboardButton(text=('✅' if accepts else '❌') + ' ' +
                                               date.strftime("%d.%m") + ' ' + time)))

            if len(kb_day) == 3:
                kb.append(kb_day)

                kb_day = []

        date = date + timedelta(days=1)

    master_free_datetime_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                                        one_time_keyboard=True, keyboard=kb)
    return master_free_datetime_keyboard

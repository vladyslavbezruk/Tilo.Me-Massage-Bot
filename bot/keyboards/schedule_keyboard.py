from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from assets.assets import *


def get_schedule_keyboard(schedule):
    kb = []

    for schedule_day in schedule.keys():
        kb_day = []

        for time in schedule[schedule_day]:
            accepts = schedule[schedule_day][time]

            (kb_day.append(KeyboardButton(text=('✅' if accepts else '❌') + ' ' +
                                               schedule_days[schedule_day] + ' ' + time)))

            if len(kb_day) == 3:
                kb.append(kb_day)

                kb_day = []

    kb_submit = [KeyboardButton(text=message_submit)]
    kb_cancel = [KeyboardButton(text=message_cancel)]

    kb.append(kb_submit)
    kb.append(kb_cancel)

    schedule_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=kb)

    return schedule_keyboard

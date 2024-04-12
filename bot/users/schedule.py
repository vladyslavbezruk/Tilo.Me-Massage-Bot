from assets.assets import *


def convert_schedule_day(day):
    for schedule_day in schedule_days.keys():
        if day == schedule_days[schedule_day]:
            return schedule_day


def get_new_schedule(old_schedule, new_schedule_param):
    new_schedule_param[1] = convert_schedule_day(new_schedule_param[1])

    user_new_schedule = old_schedule
    user_new_schedule[new_schedule_param[1]][new_schedule_param[2]] = True if new_schedule_param[0] == '❌' else False

    return user_new_schedule


DEFAULT_MASTER_SCHEDULE = {
    'monday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
               '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
               '18:00-18:55': False},
    'tuesday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
                '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
                '18:00-18:55': False},
    'wednesday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
                  '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
                  '18:00-18:55': False},
    'thursday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
                 '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
                 '18:00-18:55': False},
    'friday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
               '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
               '18:00-18:55': False},
    'saturday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
                 '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
                 '18:00-18:55': False},
    'sunday': {'10:00-10:55': False, '11:00-11:55': False, '12:00-12:55': False, '13:00-13:55': False,
               '14:00-14:55': False, '15:00-15:55': False, '16:00-16:55': False, '17:00-17:55': False,
               '18:00-18:55': False}
}

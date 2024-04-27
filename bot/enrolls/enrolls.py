import copy

import utils.files as files
from configurations.settings import *
import bot.users.users as users

from assets.assets import *

enrolls_file_path = os.path.join(PROJECT_DIR, 'database', 'enrolls', 'enrolls.json')

enrolls = []


def load_enrolls():
    global enrolls

    enrolls = files.load_file(enrolls_file_path)

    return enrolls


def create():
    global enrolls

    enrolls = []


def save_enrolls():
    files.save_file(enrolls, enrolls_file_path)


def add_enroll(status, client_tg_id, master_tg_id, category, date_view, date, time):
    enroll = {
        'id': '#' + str(len(enrolls)),
        'status': status,
        'client_tg_id': client_tg_id,
        'master_tg_id': master_tg_id,
        'category': category,
        'date_view': date_view,
        'date': date,
        'time': time
    }

    enrolls.append(enroll)

    save_enrolls()


def set_value(settings_find_by, setting_set, value_set):
    for enroll in enrolls:
        flag = True

        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                flag = False
                break

        if flag:
            enroll[setting_set] = value_set
            break

    save_enrolls()


def get_value(settings_find_by, setting_get):
    for enroll in enrolls:
        flag = True

        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                flag = False
                break

        if flag:
            return enroll[setting_get]

    return None


def get_enrolls(settings_find_by):
    found_enrolls = []

    for enroll in enrolls:
        flag = True

        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                flag = False
                break

        if flag:
            found_enrolls.append(copy.deepcopy(enroll))

    return found_enrolls


def check_enroll(settings_find_by):
    for enroll in enrolls:
        flag = True

        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                flag = False
                break

        if flag:
            return True

    return False


def get_enroll_description(enroll):
    enroll_id = str(enroll['id'])
    category = enroll['category']
    date = enroll['date']
    time = enroll['time']
    price = str(enroll_prices[category])
    master_first_name = str(users.get(enroll['master_tg_id'], 'first_name'))
    master_last_name = str(users.get(enroll['master_tg_id'], 'last_name'))

    master_fullname = master_first_name + ' ' + master_last_name
    address = users.get(enroll['master_tg_id'], 'address')

    return ('ID: ' + enroll_id + '\n' +
            'Послуги: ' + category + '\n' +
            'Вартість: ' + price + '\n' +
            'Адреса: ' + address + '\n' +
            'Час: ' + time + '\n' +
            'Майстер: ' + master_fullname + '\n' +
            'Дата: ' + date + '\n')


load_enrolls()

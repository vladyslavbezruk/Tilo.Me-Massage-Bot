import utils.files as files
from configurations.settings import *

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
        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                continue

        enroll[setting_set] = value_set
        break

    save_enrolls()


def get_value(settings_find_by, setting_get):
    for enroll in enrolls:
        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                continue

        return enroll[setting_get]

    return None

def check_enroll(settings_find_by):
    for enroll in enrolls:
        for setting_find_by in settings_find_by:
            if enroll[setting_find_by] != settings_find_by[setting_find_by]:
                continue

        return True

    return False


load_enrolls()

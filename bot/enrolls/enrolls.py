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


def add_enroll(status, client_tg_id, master_tg_id, category, date, time):
    enroll = {
        'status': status,
        'client_tg_id': client_tg_id,
        'master_tg_id': master_tg_id,
        'category': category,
        'date': date,
        'time': time
    }

    enrolls.append(enroll)

    save_enrolls()


load_enrolls()

import utils.files as files
from configurations.settings import *

users_file_path = os.path.join(PROJECT_DIR, "database", "users", "users.json")

users = {}


def load_users():
    global users

    users = files.load_file(users_file_path)

    return users


def create():
    global users

    users = {}


def save_users():
    files.save_file(users, users_file_path)


def check_user(tg_id):
    for user in users:
        if user['tg_id'] == tg_id:
            return True
    return False


def add_user(user_type, tg_id, first_name, last_name):
    user = {
        'tg_id': tg_id,
        'user_type': user_type,
        'first_name': first_name,
        'last_name': last_name
    }

    users.append(user)

    save_users()


def search_user(tg_id):
    i = 0

    for user in users:
        if user['tg_id'] == tg_id:
            return i
        i = i + 1

    return -1


def set_value(tg_id, setting, value):
    if check_user(tg_id):
        i = search_user(tg_id)

        users[i][setting] = value

        save_users()


def get(tg_id, setting):
    if check_user(tg_id):
        i = search_user(tg_id)

        return users[i][setting]

    return None


def get_user_type(tg_id):
    return get(tg_id, 'user_type')


load_users()

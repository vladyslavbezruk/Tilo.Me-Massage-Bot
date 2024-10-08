import copy

from aiogram.filters import Command
from aiogram.types import *

from bot.keyboards.cancel_keyboard import cancel_keyboard
from bot.keyboards.enroll_keyboard import enroll_keyboard
from bot.keyboards.enroll_keyboard import get_master_names_keyboard
from bot.keyboards.register_keyboard import register_keyboard
from bot.keyboards.schedule_keyboard import get_schedule_keyboard
from bot.keyboards.enroll_keyboard import get_master_free_datetime

from bot.main import dp
from bot.keyboards.start_keyboard import start_keyboard
import bot.users.users as users
import bot.enrolls.enrolls as enrolls
import bot.users.schedule as schedule

from datetime import datetime, timedelta

from assets.assets import *


@dp.message(Command(command_start))
async def echo(message: Message):
    user_tg_id = message.from_user.id

    if not users.check_user(user_tg_id):
        await message.reply(text=user_not_found, reply_markup=register_keyboard)
    elif users.get_user_type(user_tg_id) == 'client':

        await message.reply(text=start_answer_message, reply_markup=start_keyboard)

    users.set_value(user_tg_id, 'system_last_message', 'start_answer_message')


@dp.message(lambda message: message.text == message_cancel)
async def echo(message: Message):
    await message.reply(text=cancel_answer_message, reply_markup=ReplyKeyboardRemove())

    if (users.get(message.from_user.id, 'system_last_message') in
            ['register_enter_first_name', 'register_enter_last_name', 'register_enter_address',
             'register_enter_schedule']):
        users.remove_user(message.from_user.id)

    users.set_value(message.from_user.id, 'system_last_message', 'cancel_answer_message')


@dp.message(lambda message: message.text == message_enroll)
async def echo(message: Message):
    await message.reply(text=enroll_answer_message, reply_markup=enroll_keyboard)

    users.set_value(message.from_user.id, 'system_last_message', 'enroll_answer_message')


@dp.message(lambda message: message.text == message_view_enrolls)
async def echo(message: Message):
    user_tg_id = message.from_user.id

    if not enrolls.check_enroll({
        'client_tg_id': user_tg_id,
        'status': 'opened'
    }):
        await message.reply(text=message_view_enrolls_answer_no_enrolls)

        await message.reply(text=start_answer_message, reply_markup=start_keyboard)

        users.set_value(user_tg_id, 'system_last_message', 'start_answer_message')
    else:
        found_enrolls = enrolls.get_enrolls({
            'client_tg_id': user_tg_id,
            'status': 'opened'
        })

        for enroll in found_enrolls:
            enroll_description = enrolls.get_enroll_description(enroll)

            await message.reply(text=enroll_description)


@dp.message(lambda message: message.text in enroll_options)
async def echo(message: Message):
    category = message.text

    await message.reply(text=chosen_enroll_options_answer_message + category)

    master_names_keyboard = get_master_names_keyboard()

    if master_names_keyboard is None:
        await message.reply(text=chosen_enroll_options_answer_message2_no_masters, reply_markup=cancel_keyboard)
    else:
        await message.reply(text=chosen_enroll_options_answer_message2, reply_markup=get_master_names_keyboard())

        client_tg_id = message.from_user.id

        enrolls.add_enroll('last_edited', client_tg_id, '', category, '', '', '')

    users.set_value(message.from_user.id, 'system_last_message', 'chosen_enroll_options_answer_message2')


@dp.message(
    lambda message: users.get(message.from_user.id, 'system_last_message') == 'chosen_enroll_options_answer_message2')
async def echo(message: Message):
    client_tg_id = message.from_user.id
    master_full_name = message.text
    master_tg_id = users.get_tg_id_by_full_name(master_full_name)
    date_view = (datetime.now() + timedelta(days=1)).date()

    enrolls.set_value(
        {'client_tg_id': client_tg_id, 'status': 'last_edited'},
        'master_tg_id', master_tg_id)

    enrolls.set_value(
        {'client_tg_id': client_tg_id, 'status': 'last_edited'},
        'date_view', date_view.strftime("%d.%m.%Y"))

    await message.reply(text=chosen_enroll_options_answer_message3,
                        reply_markup=get_master_free_datetime(master_tg_id, date_view))

    users.set_value(message.from_user.id, 'system_last_message', 'chosen_enroll_options_answer_message3')


@dp.message(
    lambda message: users.get(message.from_user.id, 'system_last_message') == 'chosen_enroll_options_answer_message3')
async def echo(message: Message):
    client_tg_id = message.from_user.id
    master_tg_id = enrolls.get_value(
        {'client_tg_id': client_tg_id, 'status': 'last_edited'},
        'master_tg_id')

    user_answer = message.text

    date_view = datetime.strptime(
        enrolls.get_value(
            {'client_tg_id': client_tg_id, 'status': 'last_edited'},
                'date_view'),
        "%d.%m.%Y").date()

    changed_date_view = False

    if user_answer == master_free_datetime_keyboard_next_week:
        date_view = date_view + timedelta(days=7)
        changed_date_view = True
    if user_answer == master_free_datetime_keyboard_prev_week:
        date_view = date_view - timedelta(days=7)
        changed_date_view = True
    if user_answer == master_free_datetime_keyboard_next_month:
        date_view = date_view + timedelta(days=30)
        changed_date_view = True
    if user_answer == master_free_datetime_keyboard_prev_month:
        date_view = date_view - timedelta(days=30)
        changed_date_view = True

    if changed_date_view:
        await message.reply(text=chosen_enroll_options_answer_message3,
                            reply_markup=get_master_free_datetime(master_tg_id, date_view))

        enrolls.set_value(
            {'client_tg_id': client_tg_id, 'status': 'last_edited'},
            'date_view', date_view.strftime("%d.%m.%Y"))

        return

    datetime_enroll = user_answer.split(" ")

    if datetime_enroll[0] == "❌":
        await message.reply(text=chosen_enroll_options_answer_message3_error)

        await message.reply(text=chosen_enroll_options_answer_message3,
                            reply_markup=get_master_free_datetime(master_tg_id, date_view))
    else:
        date_enroll = datetime_enroll[1] + '.' + str(datetime.now().year)
        time_enroll = datetime_enroll[2]

        enrolls.set_value(
            {'client_tg_id': client_tg_id, 'status': 'last_edited'},
            'date', date_enroll)

        enrolls.set_value(
            {'client_tg_id': client_tg_id, 'status': 'last_edited'},
            'time', time_enroll)

        await message.reply(text=chosen_enroll_options_answer_message4 + date_enroll + ' ' + time_enroll)

        enrolls.set_value(
            {'client_tg_id': client_tg_id, 'status': 'last_edited'},
            'status', 'opened')

        user_tg_id = client_tg_id

        if users.get_user_type(user_tg_id) == 'client':
            await message.reply(text=start_answer_message, reply_markup=start_keyboard)

        users.set_value(user_tg_id, 'system_last_message', 'start_answer_message')


@dp.message(lambda message: message.text == register_keyboard_client)
async def echo(message: Message):
    user_tg_id = message.from_user.id

    users.add_user('client', user_tg_id, '', '', '', {},
                   'register_enter_first_name')

    await message.reply(text=register_enter_first_name, reply_markup=cancel_keyboard)

    users.set_value(user_tg_id, 'system_last_message', 'register_enter_first_name')


@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'register_enter_first_name')
async def echo(message: Message):
    if message.text != message_cancel:
        user_tg_id = message.from_user.id

        user_first_name = message.text

        users.set_value(user_tg_id, 'first_name', user_first_name)

        await message.reply(text=register_enter_last_name, reply_markup=cancel_keyboard)

        users.set_value(user_tg_id, 'system_last_message', 'register_enter_last_name')


@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'register_enter_last_name')
async def echo(message: Message):
    if message.text != message_cancel:
        user_tg_id = message.from_user.id

        user_second_name = message.text

        users.set_value(user_tg_id, 'last_name', user_second_name)

        if users.get(user_tg_id, "user_type") == "client":
            await message.reply(text=register_completed_answer_message)

            await message.reply(text=start_answer_message, reply_markup=start_keyboard)

            users.set_value(user_tg_id, 'system_last_message', 'start_answer_message')
        else:
            await message.reply(text=register_enter_address, reply_markup=cancel_keyboard)

            users.set_value(user_tg_id, 'system_last_message', 'register_enter_address')


@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'register_enter_address')
async def echo(message: Message):
    if message.text != message_cancel:
        user_tg_id = message.from_user.id

        user_address = message.text

        users.set_value(user_tg_id, 'address', user_address)

        user_schedule = users.get(user_tg_id, "schedule")

        await message.reply(text=register_enter_schedule, reply_markup=get_schedule_keyboard(user_schedule))

        users.set_value(user_tg_id, 'system_last_message', 'register_enter_schedule')


@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'register_enter_schedule')
async def echo(message: Message):
    user_tg_id = message.from_user.id

    if message.text == message_submit and users.get(user_tg_id, "schedule"):
        if users.get(user_tg_id, "schedule") != schedule.DEFAULT_MASTER_SCHEDULE:
            await message.reply(text=register_completed_answer_message, reply_markup=ReplyKeyboardRemove())
        else:
            user_schedule = users.get(user_tg_id, "schedule")

            await message.reply(text=register_enter_schedule, reply_markup=get_schedule_keyboard(user_schedule))
    else:
        new_schedule_param = message.text.split(' ')
        user_new_schedule = schedule.get_new_schedule(users.get(user_tg_id, "schedule"), new_schedule_param)

        users.set_value(user_tg_id, 'schedule', user_new_schedule)

        user_schedule = users.get(user_tg_id, "schedule")

        await message.reply(text=register_enter_schedule, reply_markup=get_schedule_keyboard(user_schedule))


@dp.message(lambda message: message.text == register_keyboard_master)
async def echo(message: Message):
    user_tg_id = message.from_user.id

    user_schedule = copy.deepcopy(schedule.DEFAULT_MASTER_SCHEDULE)

    users.add_user('master', user_tg_id, '', '', '', user_schedule,
                   'register_enter_first_name')

    await message.reply(text=register_enter_first_name, reply_markup=cancel_keyboard)

    users.set_value(user_tg_id, 'system_last_message', 'register_enter_first_name')


@dp.message(lambda message: message.text)
async def echo(message: Message):
    await message.reply(text=unknown_command_answer_message)

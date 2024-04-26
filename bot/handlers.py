import copy

from aiogram.filters import Command
from aiogram.types import *

from bot.keyboards.cancel_keyboard import cancel_keyboard
from bot.keyboards.enroll_keyboard import enroll_keyboard
from bot.keyboards.enroll_keyboard import get_master_names_keyboard
from bot.keyboards.register_keyboard import register_keyboard
from bot.keyboards.schedule_keyboard import get_schedule_keyboard

from bot.main import dp
from bot.keyboards.start_keyboard import start_keyboard
import bot.users.users as users
import bot.users.schedule as schedule

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
    await message.reply(text='Coming soon ...', reply_markup=ReplyKeyboardRemove())


@dp.message(lambda message: message.text in enroll_options)
async def echo(message: Message):
    category = message.text

    await message.reply(text=chosen_enroll_options_answer_message + category)

    master_names_keyboard = get_master_names_keyboard()

    if master_names_keyboard is None:
        await message.reply(text=chosen_enroll_options_answer_message2_no_masters, reply_markup=cancel_keyboard)
    else:
        await message.reply(text=chosen_enroll_options_answer_message2, reply_markup=get_master_names_keyboard())

    users.set_value(message.from_user.id, 'system_last_message', 'chosen_enroll_options_answer_message2')

@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'chosen_enroll_options_answer_message2')
async def echo(message: Message):
    await message.reply(text=chosen_enroll_options_answer_message3, reply_markup=cancel_keyboard)

    users.set_value(message.from_user.id, 'system_last_message', 'chosen_enroll_options_answer_message3')

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

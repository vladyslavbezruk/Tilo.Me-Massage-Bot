from aiogram.filters import Command
from aiogram.types import *

from bot.keyboards.cancel_keyboard import cancel_keyboard
from bot.keyboards.enroll_keyboard import enroll_keyboard
from bot.keyboards.register_keyboard import register_keyboard
from bot.main import dp
from bot.keyboards.start_keyboard import start_keyboard
import bot.users.users as users

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

    await message.reply(text=chosen_enroll_options_answer_message2)

    users.set_value(message.from_user.id, 'system_last_message', 'chosen_enroll_options_answer_message2')

@dp.message(lambda message: message.text == register_keyboard_client)
async def echo(message: Message):
    user_tg_id = message.from_user.id

    users.add_user('client', user_tg_id, '', '',
                   'register_enter_first_name')

    await message.reply(text=register_enter_first_name, reply_markup=cancel_keyboard)

    users.set_value(user_tg_id, 'system_last_message', 'register_enter_first_name')

@dp.message(lambda message: users.get(message.from_user.id, 'system_last_message') == 'register_enter_first_name')
async def echo(message: Message):
    if message.text == message_cancel:
        await message.reply(text=cancel_answer_message)

        users.set_value(message.from_user.id, 'system_last_message', 'cancel_answer_message')
    else:
        user_tg_id = message.from_user.id

        user_first_name = message.text

        users.set_value(user_tg_id, 'first_name', user_first_name)

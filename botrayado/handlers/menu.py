from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.handlers.config import COMMANDS, COMMANDS_2
from botrayado.handlers.schedule import RESULTS
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler


@database_handler()
async def start(msg: types.Message):
    COMMANDS_2.clear()
    RESULTS.clear()
    COMMANDS.clear()
    await msg.answer('Выберите команду', reply_markup=START_KB)


def register_handlers_menu(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        start, filters.Text(contains='Меню', ignore_case=True))
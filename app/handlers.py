from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message, ReplyKeyboardRemove

from .database import get_data
from .keyboards import menu_keyboard,complist_keyboard, BUTTON_LIST_COMPONETS, COMPlistsCallback
from .schemas_components import components
from .commands import LISTS_COMMAND

from .logging_tool import async_log_handlers, logging


router = Router()
DATABASE_lists = "datas/data_lists.json"
standart_message = "the first 3 in a small budget, the next 3 in a medium budget, the following 3 in a big budget"
standart_message_videocard = "the first 3 are in the middle budget, the next 3 are in the big budget"

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привіт, {message.from_user.full_name}!", reply_markup=menu_keyboard()
    )


@router.message(Command(LISTS_COMMAND))
@router.message(F.text == BUTTON_LIST_COMPONETS)
@async_log_handlers
async def lists(message: Message, *args, **kwargs) -> None:
    data = get_data(DATABASE_lists)
    markup_lists = complist_keyboard(data)
    await message.answer(f"Оберіть список :", reply_markup=markup_lists)


@router.callback_query(COMPlistsCallback.filter())
async def list_callback(callback: CallbackQuery, callback_data: COMPlistsCallback):
    if callback_data.title == "cooling":
        data = get_data(file_path="datas/data_cooling.json", )  # list / dict
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "frame":
        data = get_data(file_path="datas/data_frame.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "hdd":
        data = get_data(file_path="datas/data_hdd.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "motherboard":
        data = get_data(file_path="datas/data_motherboard.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "power supply unit":
        data = get_data(file_path="datas/data_power.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "processor":
        data = get_data(file_path="datas/data_processor.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "RAM":
        data = get_data(file_path="datas/data_RAM.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "ssd":
        data = get_data(file_path="datas/data_ssd.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message)
    elif callback_data.title == "video card":
        data = get_data(file_path="datas/data_videocard.json", )
        await callback.message.reply(f"info: {data}")
        await callback.message.reply(standart_message_videocard)
    await callback.answer()


@router.message()
async def echo_handler(message: Message):
    await message.reply("no such command exists")
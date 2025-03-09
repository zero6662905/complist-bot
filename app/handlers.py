from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from .database import get_data
from .keyboards import menu_keyboard,complist_keyboard, BUTTON_LIST_COMPONETS, ComponentsCallBack
from .schemas_components import components
from .commands import LISTS_COMMAND

from .logging_tool import async_log_handlers, logging


router = Router()
DATABASE_lists = "data_lists.json"


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





@router.message()
async def echo_handler(message: Message):
    await message.reply("no such command exists")
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

BUTTON_LIST_COMPONETS = "Перелік комплектуючих"


class COMPlistsCallback(CallbackData, prefix="lists", sep=";"):
    id: int
    title: str


def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=BUTTON_LIST_COMPONETS)
    markup = builder.as_markup()
    markup.resize_keyboard = True
    return markup


def complist_keyboard(list_comp: list):
    builder = InlineKeyboardBuilder()

    for id, data_comp in enumerate(list_comp):
        callback = COMPlistsCallback(id=id, title=data_comp["title"])
        builder.button(text=callback.title, callback_data=callback.pack())
        builder.adjust(3, repeat=True)
    return builder.as_markup()

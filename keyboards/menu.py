from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get_button_start():

    builder = InlineKeyboardBuilder()

    builder.button(text="Начать", callback_data="start_anketa")

    return builder.as_markup()
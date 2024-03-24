from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from src.bot.filters.callback_filters import MyCallback


def template_inline_markup_1() -> InlineKeyboardMarkup:

    kb = [
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com"),
        ],
        [
            InlineKeyboardButton(text="222", url="https://www.youtube.com"),
            InlineKeyboardButton(text="333", url="https://www.youtube.com")
        ],
        [
            InlineKeyboardButton(text="444", url="https://www.youtube.com"),
            InlineKeyboardButton(text="555", url="https://www.youtube.com"),
            InlineKeyboardButton(text="666", url="https://www.youtube.com")
        ],
    ]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb,
    )
    return keyboard


lst = ['xxx', 'yyy', 'zzz', 'sss']  # Пример данных, возвращаемых из БД

async def template_inline_markup_2():
    keyboard = InlineKeyboardBuilder()
    for elem in lst:
        keyboard.add(InlineKeyboardButton(text=elem, url="https://www.youtube.com"))
    return keyboard.adjust(2).as_markup()


async def template_inline_markup_3() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="kkk", url="https://www.youtube.com")
    kb.button(text="www", url="https://www.youtube.com")
    kb.button(text="rrr", url="https://www.youtube.com")
    kb.adjust(3)
    return kb.as_markup()

# =======================================================================================


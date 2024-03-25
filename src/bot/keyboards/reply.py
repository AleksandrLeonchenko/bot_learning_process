from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def template_reply_markup_1() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="111"),
        ],
        [
            KeyboardButton(text="222"),
            KeyboardButton(text="333")
        ],
        [
            KeyboardButton(text="444"),
            KeyboardButton(text="555"),
            KeyboardButton(text="666")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите нужную кнопку"
    )
    return keyboard


lst = ['xxx', 'yyy', 'zzz', 'sss']  # Пример данных, возвращаемых из БД


async def template_reply_markup_2() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for elem in lst:
        keyboard.add(KeyboardButton(text=elem))
    return keyboard.adjust(3).as_markup(resize_keyboard=True, input_field_placeholder="Выберите нужную кнопку")


async def template_reply_markup_3() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="ttt")
    kb.button(text="sss")
    kb.button(text="fff")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)


# =================================================================================================

# sss = ['База', 'PostgreSQL и др.', 'Docker и др.', 'Pandas и др.', 'ML']  # Пример данных, возвращаемых из БД


def start_markup() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="Запустить бота"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Нажмите 'Запустить бота', чтобы запустить бота"
    )
    return keyboard

async def choice_activity_1(sss) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for elem in sss:
        keyboard.add(KeyboardButton(text=elem))
    return keyboard.adjust(3).as_markup(resize_keyboard=True, input_field_placeholder="Выберите нужную кнопку")

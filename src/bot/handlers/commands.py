import asyncio
from sqlalchemy.orm import session, Session
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.keyboards.inline import template_inline_markup_1
from src.bot.keyboards.reply import template_reply_markup_1

command_router = Router()


@command_router.message(Command("start1"))
async def cmd_start(message: Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=template_reply_markup_1()
    )


@command_router.message(Command('help1'))
async def help_handler(message: Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=template_inline_markup_1()
    )


# ====================================================================================


import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.bot.dispatcher import get_dispatcher
from src.configuration import conf

# from src.db.database import create_async_engine


logging.basicConfig(level=logging.INFO)


async def start_bot():
    """This function will start bot with polling mode."""
    bot = Bot(token=conf.bot.token)

    dp = get_dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging_level)
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Exit')

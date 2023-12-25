from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

from config import BOT_TOKEN

import logging


async def main():

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    from handlers import main_router_user
    dp.include_routers(
        main_router_user,
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

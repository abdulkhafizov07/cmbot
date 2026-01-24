import asyncio
import logging
import sys

from application import bot, dp
from handlers import *  # noqa
from routers import main_router


async def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    dp.include_router(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

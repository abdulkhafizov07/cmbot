import logging
import sys

from aiogram import Bot
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from application import bot, dp
from config import settings
from handlers import *  # noqa
from routers import main_router


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f"{settings.base_webhook_url}{settings.webhook_path}",
        secret_token=settings.webhook_secret,
    )


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    dp.include_router(main_router)

    dp.startup.register(on_startup)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=settings.webhook_secret,
    )

    webhook_requests_handler.register(app, path=settings.webhook_path)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=settings.web_server_host, port=settings.web_server_port)


if __name__ == "__main__":
    main()

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import settings

bot_properties = DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
bot = Bot(settings.token, default=bot_properties)
dp = Dispatcher()
asched = AsyncIOScheduler()

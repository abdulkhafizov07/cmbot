from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.mongo import MongoStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings

mongo_client = AsyncIOMotorClient(
    settings.mongo_url,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=10000,
    maxPoolSize=2,
    minPoolSize=0,
    maxIdleTimeMS=60000,
    heartbeatFrequencyMS=3600_000,
)

storage = MongoStorage(mongo_client)

bot_properties = DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
bot = Bot(settings.token, default=bot_properties)

dp = Dispatcher(storage=storage)

jobstores = {
    "default": RedisJobStore(
        host=settings.redis_url.host,
        port=settings.redis_url.port,
        db=settings.redis_database,
        password=settings.redis_url.password,
    )
}

appsched = AsyncIOScheduler(jobstores=jobstores)

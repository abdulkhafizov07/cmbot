from aiogram import Bot
from aiogram.types.bot_command import BotCommand

BOT_COMMANDS = [
    BotCommand(
        command="start", description="Botni ishga tushirish va boshlash buyrug'i"
    ),
    BotCommand(command="channels", description="Siz ulagan barcha kanallar ro‘yxati"),
    BotCommand(
        command="settings", description="Asosiy sozlamalarni ko‘rish va o‘zgartirish"
    ),
    BotCommand(command="about", description="Bot haqida to‘liq ma’lumotlarni ko‘rish"),
    BotCommand(
        command="help", description="Botdan foydalanish bo‘yicha batafsil yordam"
    ),
]


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(BOT_COMMANDS)

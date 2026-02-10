from aiogram import F
from aiogram.filters.command import Command
from aiogram.filters.logic import or_f
from aiogram.types.message import Message

from routers import main_router as rt

MY_CHANNELS_MESSAGE = """*Mening kanallarim*
_Bu yerda bo'tga ulangan kanallar chiqadi_

%(channels)s"""


@rt.message(or_f(Command("channels"), F.text == "🚀 Kanallarim"))
async def channels_handler(message: Message) -> None:
    await message.answer(
        MY_CHANNELS_MESSAGE % {"channels": "Hozircha kanllar qo'shilmagan"}
    )

from aiogram import F
from aiogram.filters.command import Command
from aiogram.filters.logic import or_f
from aiogram.types.message import Message

from keyboards.help_options import HELP_OPTIONS_KEYBOARD
from routers import main_router as rt

HELP_MESSAGE = """*Yordam olish/berish*
_Ushbu bo'tni qanday ishlatish bo'yicha yoriqnoma va admin bilan bog'lanish_


* Bu yerda kamandalar bo'ladi*

_Agar bot haqida so'ramoqchi bo'lsangiz F.A.Q tugmasiga bosishingiz mumkin. U yerda tez-tez so'raladigan savollarni yig'ib qo'yganmin_
"""


@rt.message(or_f(Command("help"), F.text == "⭐️ Yordam"))
async def help_handler(message: Message) -> None:
    await message.answer(
        HELP_MESSAGE,
        reply_markup=HELP_OPTIONS_KEYBOARD,
    )

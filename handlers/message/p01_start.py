from aiogram.filters.command import CommandStart
from aiogram.types.message import Message

from keyboards import MAIN_MENU_KEYBOARD
from routers import main_router as rt
from utils import get_full_name

WELCOME_MESSAGE = """*Assalomu alaykum*

_%(fullname)s bo'tga xush kelibsiz!_


---
_Bot hozirda *DEVELOPMENT* jarayonida (yani bot ustida ancha ishlash kerak)_
"""


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    assert message.from_user, "message.from_user can not me None value"

    fullname = await get_full_name(message.from_user)

    await message.answer(
        WELCOME_MESSAGE % {"fullname": fullname}, reply_markup=MAIN_MENU_KEYBOARD
    )

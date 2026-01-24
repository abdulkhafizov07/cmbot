from aiogram.types.message import Message

from routers import main_router as rt


@rt.message()
async def any_message_handler(message: Message) -> None:
    pass

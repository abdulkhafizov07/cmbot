from aiogram import F
from aiogram.types.callback_query import CallbackQuery

from routers import main_router as rt

AI_HELP_MESSAGE = "Botga AI hali to'liq integratsiya qilingani yo'q va o'z AI miz ustida ishlamoqdamiz"


@rt.callback_query(F.data == "require_ai_help")
async def help_handler(query: CallbackQuery) -> None:
    await query.message.answer(
        AI_HELP_MESSAGE,
    )
    await query.answer("Botga AI to'liq integratsiya qilinmagan")

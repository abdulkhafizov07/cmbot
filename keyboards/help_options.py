from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_help_options_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text="🎯 AI yordami", callback_data="require_ai_help")
    builder.button(text="✔️ F.A.Q", callback_data="request_faq_help")
    builder.button(text="💬 Admin yordami", callback_data="require_admin_help")

    builder.adjust(2)

    return builder.as_markup()


HELP_OPTIONS_KEYBOARD = get_help_options_keyboard()

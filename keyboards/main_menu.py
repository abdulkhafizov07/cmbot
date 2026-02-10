from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="🚀 Kanallarim")
    builder.button(text="🛸 Guruhlarim")

    builder.button(text="🛠 Funksiyalar")

    builder.button(text="⚙️ Sozlamalar")
    builder.button(text="ℹ️ Bot haqida")
    builder.button(text="⭐️ Yordam")

    builder.adjust(2, 1, 3)

    return builder.as_markup()


MAIN_MENU_KEYBOARD = get_main_menu_keyboard()

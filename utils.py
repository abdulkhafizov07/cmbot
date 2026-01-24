from aiogram.types.user import User


async def get_full_name(message_user: User) -> str:
    result = (
        " ".join(
            [i for i in {message_user.first_name, message_user.last_name} if i]
        ).strip()
        or message_user.username
        or "Anonymous"
    )

    return result

from application import bot


async def send_test_message(chat_id: int):
    await bot.send_message(
        chat_id=chat_id, text="This is test message from appscheduler!"
    )

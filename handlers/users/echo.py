from aiogram import types
from loader import dp, bot

from data import config

# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    await bot.send_message(chat_id=config.GROUP, text=message.text)

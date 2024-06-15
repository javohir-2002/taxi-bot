from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text

from data import config

# Echo bot
@dp.message_handler(Text("chatid"))
async def bot_echo(message: types.Message):
    await bot.send_message(message.chat.id, text=message)

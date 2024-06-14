from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.filter_prived import IsPrivate

from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))

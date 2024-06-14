from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters.filter_prived import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

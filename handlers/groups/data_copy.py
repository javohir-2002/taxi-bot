import re
from aiogram import types
from filters.filter_group import IsGroup
from loader import dp, bot
from data import config, texts



# Funktsiya, regulyar ifoda orqali so'zni tekshiradi
def check_words(text, words):
    return any(re.search(rf'\b\w*{word}\w*\b', text, re.IGNORECASE) for word in words)

# Echo bot
@dp.message_handler(IsGroup(), lambda message: check_words(message.text, texts.ALL_WORDS))
async def bot_echo(message: types.Message):
    await bot.send_message(chat_id=config.GROUP, text=message.text)

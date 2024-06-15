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
    user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>'
    text_with_link = f"{message.text}\n\n👤<b>Yo'lovchi:</b> {user_link}"
    await bot.send_message(chat_id=config.GROUP, text=text_with_link, parse_mode='HTML')


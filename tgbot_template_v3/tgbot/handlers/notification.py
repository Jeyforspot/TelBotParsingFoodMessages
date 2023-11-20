import json
import string

from aiogram import types, Router, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter

from tgbot.infrastructure.db import sql_get_users, sql_get_words
from tgbot.services import broadcaster

notification_router = Router()


@notification_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message, bot: Bot):
    check = await check_message(message)
    column_values = sql_get_users()
    user_ids = [row[0] for row in column_values]
    if check:
        # for user_id in sql_get_users():
        await broadcaster.broadcast(bot, user_ids, "Поспішайте. Хтось щось роздає!")
            # await bot.forward_message(chat_id=414533539, from_chat_id=message.chat.id, message_id=message.message_id)
            # await bot.send_message(chat_id=414533539, text="Поспішайте. Хтось щось роздає!", parse_mode=ParseMode.MARKDOWN_V2)
            # await bot.send_message(chat_id=414533539, text="===================================================")
        # from .admin import PRIVATE_NOTIFICATION
        # if PRIVATE_NOTIFICATION:
        #     text = ["[Вадя вже повідомлений\. Він поспішає до вас\!](tg://user?id=414533539)", "t\.me/gurt11chat"]
        #
        #     await bot.forward_message(chat_id=414533539, from_chat_id=message.chat.id, message_id=message.message_id)
        #     await bot.send_message(chat_id=414533539, text="\n".join(text), parse_mode=ParseMode.MARKDOWN_V2)
        #     await bot.send_message(chat_id=414533539, text="===================================================")
        #
        # else:
        #     await message.answer(text="[Вадя вже повідомлений\. Він поспішає до вас\!](tg://user?id=414533539)",
        #                          parse_mode=ParseMode.MARKDOWN_V2)

async def check_message(message: types.Message):

    words_from_sql = sql_get_words()
    words = {row[0].lower() for row in words_from_sql}

    return {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
            .intersection(words)\
            != set()
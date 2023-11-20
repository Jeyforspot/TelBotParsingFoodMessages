from contextlib import suppress

from sqlite3 import IntegrityError

from random import choice

from aiogram import Router, F, types, Bot
from aiogram.filters import CommandStart, Command

from tgbot.infrastructure.db import sql_add_user, sql_delete_user

emoji_list = ["😘", "💋", "💖", "🤩", "🤑", "❤️‍🔥", "👌"]

user_router = Router()


@user_router.message(CommandStart())
async def command_start(message: types.Message):
    text = ["Вітаю, звичайний користувач!",
            "Всі доступні команди: /all",
            "Для отримання повідомлень про їжу, прошу зареєструватися за наступною командою: /register"]
    await message.reply("\n".join(text))


@user_router.message(Command("all"))
async def command_all(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    text = ["/start - Для перезапуску бота",
            "/all - Для отримання пояснень всіх команд",
            "/register - Для реєстрації на отримання повідомлень про їжу",
            "/delete_register - Для видалення реєстрації на бота",
            "/about - Про призначення бота та розробника"]
    await bot.send_message(chat_id=user_id, text="\n".join(text))

@user_router.message(Command("register"))
async def command_register(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    try:
        sql_add_user(user_id)
        await bot.send_message(chat_id=user_id, text=f"Ви успішно зареєструвалися. Тепер ви будете отримувати сповіщення про їжу {choice(emoji_list)}")
    except IntegrityError:
        await bot.send_message(chat_id=user_id, text="Ви вже зареєстровані. Якщо хочете припинити отримувати сповіщення від бота, введіть /delete_register")


@user_router.message(Command("delete_register"))
async def command_delete_register(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    num_rows_affected = sql_delete_user(user_id)
    if num_rows_affected:
        await bot.send_message(chat_id=user_id, text=f"Ви успішно припинили отримання повідомлення {choice(emoji_list)}")
    else:
        await bot.send_message(chat_id=user_id, text=f"У вас немає в базі людей для розсилки. Для реєстрації введіть /register")


@user_router.message(Command("about"))
async def command_about_register(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    text = ["Бот призначений для розсилання повідомлень, про безкоштовну роздачу предметів/їжі/т.п. "
            "в чаті гуртожитку", "Бот в беті, тому може зреагувати не на всі роздачі або зреагувати хибно",
            "Розробник: https://t.me/But_I_am_a_baka"]
    await bot.send_message(chat_id=user_id, text="\n".join(text))

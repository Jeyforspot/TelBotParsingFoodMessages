import os

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.inline import private_notification_keyboard, delete_keyboard


admin_router = Router()
admin_router.message.filter(AdminFilter())

PRIVATE_NOTIFICATION = True

@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("Wellcome, admin! /all")


@admin_router.message(Command("private_notification"))
async def admin_private_notification(message: Message):
    markup = await private_notification_keyboard()
    await message.reply(f"Hello! Do you want to turn {'off' if PRIVATE_NOTIFICATION else 'on'} PRIVATE_NOTIFICATION?",
                        reply_markup=markup)


@admin_router.message(F.text.lower() == "yes")
async def answer_YES(message: Message):
    global PRIVATE_NOTIFICATION
    PRIVATE_NOTIFICATION = False if PRIVATE_NOTIFICATION else True
    markup = await delete_keyboard()
    await message.reply(f"The PRIVATE_MODIFICATION was turn {'on' if PRIVATE_NOTIFICATION else 'off'}",
                        reply_markup=markup)


@admin_router.message(F.text.lower() == "cancel")
async def answer_Cancel(message: Message):
    markup = await delete_keyboard()
    await message.reply("Cancel", reply_markup=markup)

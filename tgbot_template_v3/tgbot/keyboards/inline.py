from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


async def private_notification_keyboard():
    keyboard = [
        [KeyboardButton(text="YES")],
        [KeyboardButton(text="Cancel")]
    ]
    markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Are you sure?"
    )
    return markup


async def delete_keyboard():
    return ReplyKeyboardRemove()

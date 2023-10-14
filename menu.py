from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def dynamic_reply_kb(text_button):

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text_button[0])]
        ],
        resize_keyboard=True
    )

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("I LOST")
        ],
        [
            KeyboardButton("I FEEL BAD")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
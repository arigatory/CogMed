from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

management = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Tools")
        ],
        [
            KeyboardButton("Rules")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
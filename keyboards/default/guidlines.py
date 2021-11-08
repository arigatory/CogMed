from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

guidelines = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Communication rules")
        ],
        [
            KeyboardButton("Living place")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
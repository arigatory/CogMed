from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

doctors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Main menu")
        ],
        [
            KeyboardButton("Medical records")
        ],
        [
            KeyboardButton("Guidelines")
        ],
        [
            KeyboardButton("Updates")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
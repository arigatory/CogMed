from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

red_flags = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Dangerous symptoms")
        ],
        [
            KeyboardButton("Dangerous adverse effects")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
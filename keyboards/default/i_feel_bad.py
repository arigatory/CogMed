from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

i_feel_bad = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Emergency")
        ],
        [
            KeyboardButton("Call my relatives")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
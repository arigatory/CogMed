from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

i_lost = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("EMERGENCY")
        ],
        [
            KeyboardButton("Share your geoposition")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
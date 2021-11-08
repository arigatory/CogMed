from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

medications = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Tablets count")
        ],
        [
            KeyboardButton("My reminders")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
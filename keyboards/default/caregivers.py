from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

caregivers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Guidelines")
        ],
        [
            KeyboardButton("Cognitive training")
        ],
        [
            KeyboardButton("Red flags")
        ],
        [
            KeyboardButton("Management")
        ],
        [
            KeyboardButton("Medical records")
        ],
        [
            KeyboardButton("Psychological support")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)
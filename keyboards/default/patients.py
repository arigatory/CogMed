from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

patients = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Medications")
        ],
        [
            KeyboardButton("Cognitive training")
        ],
        [
            KeyboardButton("Complaints")
        ],
        [
            KeyboardButton("Help")
        ],
        [
            KeyboardButton("Cancel")
        ],
    ],
    resize_keyboard=True
)

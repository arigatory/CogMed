from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👩‍⚕️ 👨‍⚕️ Doctors")
        ],
        [
            KeyboardButton("👀 Caregivers")
        ],
        [
            KeyboardButton("👴👵 Patients")
        ]
    ],
    resize_keyboard=True
)
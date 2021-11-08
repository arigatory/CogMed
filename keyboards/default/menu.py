from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🩺 Консультация"),
            KeyboardButton("😷 Помощь по симптому"),
        ],
[
            KeyboardButton("🔍 Расшифровать анализы"),
            KeyboardButton("👩‍⚕️Персональное ведение👨‍⚕️")
        ],
        [
            KeyboardButton("💊 Помощь по лечению"),
            KeyboardButton("❓Информация о болезни"),
        ],
        [
            KeyboardButton("📚 Медицинская карта"),
            KeyboardButton("👥 Второе мнение"),
        ]
    ],
    resize_keyboard=True
)
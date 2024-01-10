from aiogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup
)


links = InlineKeyboardMarkup(
  inline_keyboard= [
    [
      InlineKeyboardButton(text='a', url='http://youtube.com')
    ]
  ]
)
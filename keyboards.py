from aiogram.types import (
  ReplyKeyboardMarkup,
  KeyboardButton,
  InlineKeyboardButton,
  InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
  keyboard = [
    [
      KeyboardButton(text='Новый проект'),
      KeyboardButton(text='Продолжить'),
    ],
  ],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder='Выберите команду',
  selective=True
)

links_kb = InlineKeyboardMarkup(
  inline_keyboard= [
    [
      InlineKeyboardButton(text='afsdf')
    ]
  ]
)
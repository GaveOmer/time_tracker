from aiogram.types import (
  ReplyKeyboardMarkup,
  KeyboardButton
)


main = ReplyKeyboardMarkup(
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

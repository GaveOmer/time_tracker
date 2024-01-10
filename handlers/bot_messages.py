from aiogram import Router, F
from aiogram.types import Message
from keyboards import reply, inline

router = Router()

@router.message()
async def echo(message: Message):
  msg = message.text.lower()
  if msg == 'новый проект':
    await message.answer('Введите название вашего проекта:')
    
@router.message()
async def respond_to_project_name(message: Message):
  
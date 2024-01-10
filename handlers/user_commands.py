from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
  await message.answer(f"Привет, {message.from_user.first_name}! Это приложение для отслеживания времени, затраченного на ваши проекты. \n1. Чтобы начать, нужно создать новый проект - /newProject - /projectName и начать отслеживание - /track.\n2. Чтобы остановить отслеживание следует прописать команду /stop \n3. Чтобы продолжить отслеживание созданного проекта нужно написать команду /continue и название проекта .", reply_markup=reply.main)

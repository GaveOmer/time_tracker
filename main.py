import asyncio
import keyboards
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

API_TOKEN = '6456779280:AAEhDLhakn40yyVCd_Lhr9OhtiZ3SvUVXJo'

bot = Bot(token=API_TOKEN, parse_mode = 'HTML')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await message.answer(f"Привет, {message.from_user.first_name}! Это приложение для отслеживания времени, затраченного на ваши проекты. \n1. Чтобы начать, нужно создать новый проект - /newProject - /projectName и начать отслеживание - /track.\n2. Чтобы остановить отслеживание следует прописать команду /stop \n3. Чтобы продолжить отслеживание созданного проекта нужно написать команду /continue и название проекта .", reply_markup=keyboards.main_kb)

@dp.message()
async def echo(message: Message):
  msg = message.text.lower()
  if msg == 'новый проект':
    await message.answer('Введите название вашего проекта:', reply_markup=keyboards.links_kb)

async def main(): 
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)
  
  
  
  
  
if __name__ == '__main__':
    asyncio.run(main())

#1 команда для создания проекта
#2 команда для отслеживания проекта
#3 команда для записи проекта в базу данных, хранения данных о затраченном времени и проверки существующих проектов


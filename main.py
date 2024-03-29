import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands
from config_reader import config


async def main(): 
  bot = Bot(config.bot_token.get_secret_value(), parse_mode = 'HTML')
  dp = Dispatcher()

  dp.include_routers(
    user_commands.router,
    #callbacks
    bot_messages.router
  )

  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)
  
if __name__ == '__main__':
    asyncio.run(main())

#1 команда для создания проекта
#2 команда для отслеживания проекта
#3 команда для записи проекта в базу данных, хранения данных о затраченном времени и проверки существующих проектов
#4 команда для вывода стастики по всем проектам

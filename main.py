from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5857090034:AAHt8-3ztS9e6MZxdPRuof0UnhsYARdtQXk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Skillbox!"
                       "\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")
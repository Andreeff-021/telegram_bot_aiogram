from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboard import greet_kb
from config import TOKEN
from random import randint


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'На кону конфеты - 121 шт'
      '\nКаждый игрок берет конфеты по очереди, не более 28 шт'
      '\nКто заберёт все конфеты, тот победитель!')
    await bot.send_message(message.from_user.id, 'Нажмите "Начать"!', reply_markup=greet_kb)

@dp.message_handler(commands=['Начать'])
async def st(message: types.Message):
    player = message.from_user.full_name
    await message.answer(text=f'{player} введите число!')

    global total
    total = 121


@dp.message_handler()
async def invalid_input(message: types.Message):
    global total
    player = message.from_user.full_name
    take = int(message.text)
    if take <= 0 or take > 28 or take > total:
        await message.answer(text='Некорректный ввод!')
    else:
        total -= take
        if total == 0:
            await message.answer(text=f'{player} вы победитель!'
                                      f'\nЧтобы начать игру снова, нажмите "Начать"', reply_markup=greet_kb)
        else:
            await message.answer(text=f'Конфет осталось {total}')
            cpu = randint(1, 28)
            if cpu > total:
                cpu = randint(1, total)
                total -= cpu
            else:
                total -= cpu
            await message.answer(text=f'Компьютер взял {cpu}.\nКонфет осталось {total}')

            if total == 0:
                await message.answer(text=f'Компьютер выиграл!'
                                          f'\nЧтобы начать игру снова, нажмите "Начать"', reply_markup=greet_kb)



if __name__ == '__main__':
    executor.start_polling(dp)
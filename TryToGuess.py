import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor

from STEP.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

TryToGuess = random.randint(100, 200)


# Команда старт
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Угадай число в интервале от 100 до 200")


# Команда "Помощь". Можно сразу узнать число
@dp.message_handler(commands='help')
async def helpme(message: types.Message):
    await bot.send_message(message.from_user.id, f"Правильное число - {TryToGuess} ")


@dp.message_handler(content_types=ContentType.TEXT)
async def checking(message: types.Message):
    text = message.text

    try:
        text = int(text)
        if text < TryToGuess:
            await bot.send_message(message.from_user.id, "Загаданное число больше!\n Пробуй ещё.")
        elif text > TryToGuess:
            await bot.send_message(message.from_user.id, "Загаданное чилсло меньше!\n Пробуй ещё.")
        else:
            await bot.send_message(message.from_user.id, "Ты угадал число!\n Это было не так уж легко.")
    except ValueError:
        await bot.send_message(message.from_user.id, "Это не число.")
        text = None


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




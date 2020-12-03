import random
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor

from .config import TOKEN   # Подключение токена

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Загаданное число. Значение меняется при перезапуске
TryToGuess = random.randint(0, 4)


# Команда "Старт"
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("Угадай число в интервале от 0 до 4", reply_markup=start_output)


# Команда "Помощь". Если очень лень нажать 4 кнопки, можно сразу узнать число
@dp.message_handler(commands='help')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Правильное число - {TryToGuess}")

#  "Инициализация" (создание экземпляра - кнопки или как это правильно назвать) и расположение кнопок
button_0 = KeyboardButton('0️⃣')
button_1 = KeyboardButton('1️⃣')
button_2 = KeyboardButton('2️⃣')
button_3 = KeyboardButton('3️⃣')
button_4 = KeyboardButton('4️⃣')
start_output = ReplyKeyboardMarkup()
start_output.add(button_1, button_2).row(button_3, button_4)
start_output.row(button_0)


# Если нажата кнопка 0
@dp.message_handler(Text(equals=["0️⃣"]))
async def pressed_0(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ты выбрал 0", reply_markup=start_output)
    if TryToGuess == 0:
        await bot.send_message(message.from_user.id, f"Угадалъ", reply_markup=start_output)
    else:
        await bot.send_message(message.from_user.id, f"Не угадал, пробуй до победы...", reply_markup=start_output)


# Если нажата кнопка 1
@dp.message_handler(Text(equals=["1️⃣"]))
async def pressed_1(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ты выбрал 1", reply_markup=start_output)
    if TryToGuess == 1:
        await bot.send_message(message.from_user.id, f"Угадалъ", reply_markup=start_output)
    else:
        await bot.send_message(message.from_user.id, f"Не угадал, пробуй до победы...", reply_markup=start_output)


# Если нажата кнопка 2
@dp.message_handler(Text(equals=["2️⃣"]))
async def pressed_2(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ты выбрал 2", reply_markup=start_output)
    if TryToGuess == 2:
        await bot.send_message(message.from_user.id, f"Угадалъ", reply_markup=start_output)
    else:
        await bot.send_message(message.from_user.id, f"Не угадал, пробуй до победы...", reply_markup=start_output)


# Если нажата кнопка 3
@dp.message_handler(Text(equals=["3️⃣"]))
async def pressed_3(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ты выбрал 3", reply_markup=start_output)
    if TryToGuess == 3:
        await bot.send_message(message.from_user.id, f"Угадалъ", reply_markup=start_output)
    else:
        await bot.send_message(message.from_user.id, f"Не угадал, пробуй до победы...", reply_markup=start_output)


# Если нажата кнопка 4
@dp.message_handler(Text(equals=["4️⃣"]))
async def pressed_4(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ты выбрал 4", reply_markup=start_output)
    if TryToGuess == 4:
        await bot.send_message(message.from_user.id, f"Угадалъ", reply_markup=start_output)
    else:
        await bot.send_message(message.from_user.id, f"Не угадал, пробуй до победы...", reply_markup=start_output)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


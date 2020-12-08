from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.utils.markdown import text

from STEP.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

init_list = []  # В этот список записываем инициалы
start_text = text("Приветствую.\nЭто бот для добавления инициалов и их вывода.",
                  "\nДля добавления или показа инициалов воспользуйтесь кнопками ниже:")

# Инлайн кнопки
btn_add_fn = InlineKeyboardButton("Добавить инициал имени", callback_data='btnf')   # fn - first name
btn_add_ln = InlineKeyboardButton("Добавить инициал фамилии", callback_data='btnl')     # ln - last name
btn_show = InlineKeyboardButton("Показать инициалы", callback_data='btns')
markup = InlineKeyboardMarkup().add(btn_add_fn, btn_add_ln).row(btn_show)
markup2 = InlineKeyboardMarkup().row(btn_add_fn, btn_add_ln, btn_show)


# Команда "Старт"
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, start_text, reply_markup=markup)


# Кнопка добавления инициала имени. В случае, если в поле имени ничего нет, вылетает TypeError,
# я ее ловлю. Других ошибок быть не должно.
@dp.callback_query_handler(lambda c: c.data == 'btnf')
async def addition_f(callback_query: types.CallbackQuery):
    try:
        initials = callback_query.from_user.first_name
        init_list.append(initials[0])
        await bot.send_message(callback_query.from_user.id, 'Инициал имени добавлен')
    except TypeError:
        await bot.send_message(callback_query.from_user.id, "Имя не введено, инициал не добавлен.\n")
        pass


# Кнопка добавления инициала фамилии. TypeError аналогично имени.
@dp.callback_query_handler(lambda c: c.data == 'btnl')
async def addition_l(callback_query: types.CallbackQuery):
    try:
        initials = callback_query.from_user.last_name
        init_list.append(initials[0])
        await bot.send_message(callback_query.from_user.id, "Инициал фамилии добавлен")
    except TypeError:
        await bot.send_message(callback_query.from_user.id, "Фамилия не введена, инициал не добавлен.")
        pass


# Кнопка показа введенных инициалов. Если список пуст, выводит "Введённых инициалов нет".
@dp.callback_query_handler(lambda c: c.data == 'btns')
async def showing(message: types.Message):
    if len(init_list) != 0:
        await bot.send_message(message.from_user.id, "Введённые инициалы:" + '. '.join(init_list))
    else:
        await bot.send_message(message.from_user.id, "Введённых инициалов нет")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor

from STEP.config import TOKEN

bot = Bot(token=TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)


class FoodOrder(StatesGroup):
    first_course_waiting = State()
    second_course_waiting = State()


# Функция для добавления кнопок. Переводит все наименования в списке в кнопки.
def add_key(avaliable_menu):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for name in avaliable_menu:
        keyboard.add(name)
    return keyboard


# Спски, где хранится меню
first_course = ["Борщ", "Кулеш", "Суп с галушками", "Капусняк", "Свекольник"]
second_course = ["Вареники", "Кутья", "Кура, фаршированая яблоками", "Голубцы", "Деруны"]


# Start. Сразу предлагает заказать еду
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привет. Я - бот для заказа еды украинской кухни. Для заказа введите команду /food")


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    waiting_for_food_size = State()


@dp.message_handler(commands="food", state="*")
async def starter_choise(message: types.Message):
    await message.answer("Выберите блюдо:", reply_markup=add_key(first_course))
    await OrderFood.waiting_for_food_name.set()


@dp.message_handler(state=OrderFood.waiting_for_food_name, content_types=types.ContentTypes.TEXT)
async def sec_choise(message: types.Message, state: FSMContext):
    text = message.text
    if text not in first_course:
        await message.reply("Пожалуйста, выберите блюдо, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_food=message.text.lower())
    await OrderFood.next()
    await message.answer("Теперь выберите размер порции:", reply_markup=add_key(second_course))


@dp.message_handler(state=OrderFood.waiting_for_food_size, content_types=types.ContentTypes.TEXT)
async def food_step_3(message: types.Message, state: FSMContext):
    text = message.text
    if text not in second_course:
        await message.reply("Пожалуйста, выберите размер порции, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_food2=message.text.lower())
    user_data = await state.get_data()
    await message.answer(f"Первым блюдом вы выбрали {user_data['chosen_food']}, вторым -  {user_data['chosen_food2']}."
                         , reply_markup=types.ReplyKeyboardRemove())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

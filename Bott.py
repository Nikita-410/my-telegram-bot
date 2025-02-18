import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = "7817114744:AAEeo536wH19PNhaZd1ckcWHgP209EetvQA"  # Замени на свой токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

users_data = {}

# Команда /start
@dp.message(Command("start"))
async def start(message: Message):
    user_id = message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {"balance": 0, "runs": 0}

    await message.answer(
        "👤 *Ваш личный кабинет:*\n\n"
        f"💰 Баланс: {users_data[user_id]['balance']} RUB\n"
        f"♻ Запусков: {users_data[user_id]['runs']}\n",
        parse_mode="Markdown"
    )

# Кнопка для запуска WebApp (майнинга)
@dp.message(lambda message: message.text == "🌀 Заработать")
async def mine(message: types.Message):
    webapp_button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            "🚀 Начать майнинг",
            web_app=WebAppInfo(url="https://127.0.0.1:5000.herokuapp.com")  # Замени на свой URL
        )
    )
    await message.answer("🚀 Запустите майнинг и зарабатывайте!", reply_markup=webapp_button)

# Получение данных от WebApp
@dp.message(lambda message: message.web_app_data)
async def receive_data(message: Message):
    user_id = message.from_user.id
    data = message.web_app_data.data

    try:
        earned = int(eval(data).get("earned", 0))
        users_data[user_id]['balance'] += earned
        users_data[user_id]['runs'] += 1
        await message.answer(f"✅ Вы заработали {earned} RUB!\n💰 Ваш баланс: {users_data[user_id]['balance']} RUB")
    except:
        await message.answer("Ошибка обработки данных!")

# Асинхронный запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command

API_TOKEN = "8035146676:AAHGG1HL8rGET5SKXt1Q1GhaN-N0JJpdGsk"
ADMIN_ID = 1150616818

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Приветственное сообщение
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте! Спасибо за сообщение. Мы скоро свяжемся с вами.")

# Обработка всех сообщений
@dp.message_handler()
async def forward_to_admin(message: types.Message):
    if str(message.from_user.id) != str(ADMIN_ID):
        msg = f"📩 Новое сообщение от @{message.from_user.username or 'без имени'} (ID: {message.from_user.id}):

{message.text}"
        await bot.send_message(ADMIN_ID, msg)

# Ответ админа
@dp.message_handler(Command("reply"))
async def reply_user(message: types.Message):
    if str(message.from_user.id) == str(ADMIN_ID):
        try:
            parts = message.text.split(" ", 2)
            user_id = int(parts[1])
            reply_text = parts[2]
            await bot.send_message(user_id, f"💬 Ответ от администратора:
{reply_text}")
            await message.reply("✅ Ответ отправлен.")
        except Exception as e:
            await message.reply(f"Ошибка: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
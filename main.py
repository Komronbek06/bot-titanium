import logging
from aiogram import Bot, Dispatcher, executor, types
import os

# Tokenni os.environ orqali olamiz (Railway uchun qulay)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Botni sozlash
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Assalomu alaykum! ✅ Bot ishlayapti.")

# Oddiy echo (yuborgan narsangni qaytaradi)
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

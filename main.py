import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Tokenni ENV dan olish
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start komandasi
@dp.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Salom! 👋 Men Aiogram 3.x botman.")

async def main():
    # Pollingni ishga tushiramiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

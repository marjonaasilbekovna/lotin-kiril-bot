from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🔥 Buyruqlar \nBotdan foydalanish uchun '/start' - tugmasini bosing va tilni tanlang... \n'/about' - Bot haqida qisqacha ma'lumot. \n'/xabar' - adminga murojatlaringizni yozib qoldirishingiz mumkin.\n'/bot_admin' - adminimiz.")

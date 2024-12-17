from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu bot orqali siz o'zingizga kerakli bo'lgan matnlarni lotin tilidan kirilchaga yoki kirilchadan lotinchaga to'g'ridan to'g'ri o'girish imkoniyatiga ega bo'lasiz.\nBu bot 'Sifatedu' o'quv markazi tomonidan yaratilgan 'Lotin Kiril' boti hisoblanadi.")


from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"Assalomu alaykum 😊   {full_name}   Latin Ciril botiga hush kelibsiz\n\nBu bot sizga lotin tilida yozilgan matnlarni kirilchaga o'girishga yoki Kirilchada yozilgan matnlarni lotinchaga o'girishga yordam beradi.\n\nKerakli tilga o'girish uchun o'girmoqchi bo'lgan matningizni kiriting ;\n\nmalumot uchun : Agar siz kirilcha matn kiritsangiz bot sizga lotinchasini, yoki lotincha matn kiritsangiz kirilchasini chiqarib beradi.")
    except:
        await message.answer(text=f"Assalomu alaykum 😊   {full_name}   Latin Ciril botiga hush kelibsiz\n\nBu bot sizga lotin tilida yozilgan matnlarni kirilchaga o'girishga yoki Kirilchada yozilgan matnlarni lotinchaga o'girishga yordam beradi.\n\nKerakli tilga o'girish uchun o'girmoqchi bo'lgan matningizni kiriting ;\n\nmalumot uchun : Agar siz kirilcha matn kiritsangiz bot sizga lotinchasini, yoki lotincha matn kiritsangiz kirilchasini chiqarib beradi.")

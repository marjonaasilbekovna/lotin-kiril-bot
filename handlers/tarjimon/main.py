from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram import F
from handlers.tarjimon.latinciril import transliter
# from aiogram.filters import Command
# from keyboard_buttons.inline.menu import menu, alishtirish

@dp.message(F.text)
async def transliter_text(message: Message):
    translation = message.text
    translation = transliter(translation)
    await message.answer(translation)

# # Tugma bosilganda ishlovchi funksiya
# @dp.callback_query(F.data == "lotin")
# async def lotincha(query: CallbackQuery):
#     await query.message.answer("Kirilchaga o'girish uchun matnni kiriting :")
    

# # Tugma bosilganda ishlovchi funksiya
# @dp.callback_query(F.data == "kiril")
# async def kirilcha(query: CallbackQuery):
#     await query.message.answer("Lotinchaga o'girish uchun matnni kiriting :")

#     # await query.answer()

# # Matnni qayta ishlash
# @dp.message()
# async def transliter_text(message: Message):
#     if message.text.isascii():  # Agar matn lotin bo'lsa
#         translation = transliter(message.text)
#         await message.answer(f"Kirilchaga o'giriligan matn :\n\n {translation}", reply_markup=alishtirish)
#     else:  # Aks holda Kirildan Lotinga
#         translation = transliter(message.text)
#         await message.answer(f"Lotinchaga o'girilgan matn :\n\n {translation}", reply_markup=alishtirish)
  

# # Orqaga tugmasi

# @dp.callback_query(F.data == "ozgartir")
# async def yana_reklama(query: CallbackQuery):
#     await query.message.delete()
#     print("Til o'zgartirildi ❤️")
#     await query.message.answer("Tilni tanlang", reply_markup=menu)

from loader import dp  # dp — Dispatcher obyekti
from aiogram.types import Message
from aiogram import F
from handlers.tarjimon.latinciril import transliter

@dp.message(F.text)
async def transliter_text(message: Message):
    translation = message.text
    translation = transliter(translation)
    await message.answer(translation)

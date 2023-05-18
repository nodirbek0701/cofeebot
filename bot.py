
from aiogram import Bot,Dispatcher,types,executor
import logging
from api import get_coffee
logging.basicConfig(level=logging.INFO)

bot=Bot(token="6283434849:AAGDm1teogqfbHLHnkKpdlKQjGr96mjoVIg")
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def salomlash(message:types.Message):
    await message.answer("Salom men senga coffe yuboraman /cofe ni bos")

@dp.message_handler(commands="cofe")
async def cofe(message:types.Message):
    rasm=get_coffee()
    await message.answer(rasm)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
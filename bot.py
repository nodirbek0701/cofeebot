
from aiogram import Bot,Dispatcher,types,executor
import logging
from api import get_coffee
logging.basicConfig(level=logging.INFO)

bot=Bot(token="6132460317:AAG6IS0Gqp01rBT-lWQk7x9bmD5D7SetYS0")
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def salomlash(message:types.Message):
    await message.answer("Salom men sizga coffe rasmlarini  yuboraman /cofe ni bosing \nHar bosganizda har hil cofe yuboraman")

@dp.message_handler(commands="cofe")
async def cofe(message:types.Message):
    rasm=get_coffee()
    await message.reply_photo(photo=rasm)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
from aiogram import Bot, Dispatcher, types, executor
from menu import dynamic_reply_kb
from aiogram.types import Message, CallbackQuery

token = '6342775865:AAHEdCF8I_Vml8qs7Ieh6EnPcG9JjGf1o2k'
bot = Bot(token)
dp = Dispatcher(bot)


text_button = [
['Winter'],['Spring'],['Sumer'],['autumn']
]
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Напишіть пору року:")

@dp.message_handler(text='Winter'.split())
async def Winter(message: types.Message):
    await message.answer('Ви обрали зиму. Можете перемкнути на наступну пору року.', reply_markup=dynamic_reply_kb(text_button[1]))

@dp.message_handler(text='Spring'.split())
async def Spring(message: types.Message):
    await message.answer('Ви обрали весну. Можете перемкнути на наступну пору року.', reply_markup=dynamic_reply_kb(text_button[2]))

@dp.message_handler(text='Sumer'.split())
async def Sumer(message: types.Message):
    await message.answer('Ви обрали літо. Можете перемкнути на наступну пору року.', reply_markup=dynamic_reply_kb(text_button[3]))

@dp.message_handler(text='autumn'.split())
async def Autumn(message: types.Message):
    await message.answer('Ви обрали осінь. Можете перемкнути на наступну пору року.', reply_markup=dynamic_reply_kb(text_button[0]))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

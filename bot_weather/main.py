import math

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests

bot = Bot(token='5728801405:AAFmxiXap3uP0gButl_AlEHg-4R58hWSME4')
api_key = 'a87e29e036ccdcb536a820d5e24011fb'
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Введите город")


@dp.message_handler()
async def echo_message(message: types.Message):
    city = message.text
    r = math.ceil(float(requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').json()['main']['temp'])-273.15)
    await bot.send_message(message.from_user.id, f"В {city} {r} температура")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

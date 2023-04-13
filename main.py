import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

token = '6228010271:AAEa9j96bN5x-7L3_pNgaGJSvYvQw8f3L-o'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

HELP = '''

все вопросы к @shindji22
'''


async def start_up(_):
    print('bot started')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Добро пожаловать. С помощью данного бота, вы сможете напрямую общаться с ChatGPT')

@dp.message_handler(commands=['help'])
async def echo(message:types.Message):
    await bot.send_message(message.from_user.id, text=HELP, reply_markup=ReplyKeyboardMarkup())

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)

    await message.answer(response['choices'][0]['text'])

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_up)
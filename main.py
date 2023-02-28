import asyncio
import random
import aiogram as aiogram
import logging
from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.types import ChatMemberAdministrator
from aiogram.dispatcher.filters import Command

API_TOKEN = '6206131801:AAGOM4hc4n9TwR-PjuXA5o3KVphW3aOVq7I'
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['name'])
async def cats(message: types.Message, command):
    if command.args:
        await bot.promote_chat_member(message.chat.id, message.from_user.id, can_pin_messages=True)
        await bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, command.args)
        await message.answer(f"привет, <b>{command.args}<b>")
    else:
        await message.answer("укажи своё имя после команды /name")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
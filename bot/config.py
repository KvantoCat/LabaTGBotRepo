import os

from dotenv import load_dotenv
from telebot.types import BotCommand
from telebot.async_telebot import AsyncTeleBot

load_dotenv()

async def set_bot_commands(bot : AsyncTeleBot):
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Помощь"),
    ]

    await bot.set_my_commands(commands)

class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

config = Config()

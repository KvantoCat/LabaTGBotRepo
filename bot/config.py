from dotenv import load_dotenv
from telebot.types import BotCommand
from telebot.async_telebot import AsyncTeleBot

import os

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    def __init__(self):
        self.commands = []

    async def set_bot_commands(self, bot : AsyncTeleBot):
        self.commands.clear()

        self.commands.append(BotCommand("start", "Запустить бота"))
        self.commands.append(BotCommand("help", "Помощь"))

        await bot.set_my_commands(self.commands)

bot_config = Config()
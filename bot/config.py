from dotenv import load_dotenv
from telebot.types import BotCommand
from telebot.async_telebot import AsyncTeleBot

import os

load_dotenv()

class Config:
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN", "")

        self.commands = [
            BotCommand("start", "Запустить бота"),
            BotCommand("help", "Помощь")
        ]

    async def set_bot_commands(self, bot : AsyncTeleBot) -> None:
        await bot.set_my_commands(self.commands)

bot_config = Config()
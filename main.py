
import asyncio
import logging

from telebot.async_telebot import AsyncTeleBot
from bot.config import config
from bot.handlers import register_handlers

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = AsyncTeleBot(config.BOT_TOKEN)

    register_handlers(bot)

    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())

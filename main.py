
import asyncio
import logging
import bot.config as bot_config

from telebot.async_telebot import AsyncTeleBot
from bot.handlers import register_handlers

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = AsyncTeleBot(bot_config.config.BOT_TOKEN)

    await bot_config.set_bot_commands(bot)

    register_handlers(bot)

    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())

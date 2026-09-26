from telebot.async_telebot import AsyncTeleBot
from bot.handlers import register_handlers
from bot.config import bot_config
from bot.data import bot_data

import asyncio
import logging

async def main():
    logging.basicConfig(level=logging.INFO)

    bot_data.parse_jokes_file()

    bot = AsyncTeleBot(bot_config.BOT_TOKEN)

    await bot_config.set_bot_commands(bot)

    register_handlers(bot)

    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())

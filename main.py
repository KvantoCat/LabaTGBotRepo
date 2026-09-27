from telebot.async_telebot import AsyncTeleBot
from bot.handlers import register_handlers
from bot.config import bot_config

import asyncio
import logging

async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = AsyncTeleBot(bot_config.bot_token)

    await bot_config.set_bot_commands(bot)

    register_handlers(bot)

    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())

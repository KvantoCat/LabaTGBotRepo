
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

def register_handlers(bot : AsyncTeleBot):

    @bot.message_handler(commands=["start"])
    async def send_welcome_message(message : Message) -> None:
        await bot.send_message(message.chat.id, "Привет!")

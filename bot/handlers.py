from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from bot import utils
from bot.data import bot_data
from PIL import Image

import emoji
import random

def register_handlers(bot : AsyncTeleBot):
    @bot.message_handler(commands=["start"])
    async def start_handler(message : Message) -> None:
        text = (
            f":green_circle:  *{utils.get_full_user_name(message)}, добро пожаловать в мем\-бота\!*  :green_circle:\n\n"
            "Здесь собраны лучшие __мемы и шутки__ на все случаи жизни\.\n"
            "Введите \"Мемы про работу\"\, \"Милые котики\"\, \"Смешные дети\" или \"Самая крутая шутка в мире\"\n\n"
            "Доступные команды\:\n"
            "/start  Запустить бота\n"
            "/help   Помощь\n\n"
            "||Выполнил Колегов Ярослав 8к64||\n"
        )

        emoji_text = emoji.emojize(text, language="alias")

        await bot.send_message(message.chat.id, emoji_text, parse_mode="MarkdownV2")

    @bot.message_handler(commands=["help"])
    async def help_handler(message : Message) -> None:
        text = (
            f"*Еще раз привет, {utils.get_full_user_name(message)}\!*\n"
            "Этот бот показывает рандомные изображения и шутки по введенным ключевым словам\.\n"
            "Есть мемы по тематикам\: коты, работа, дети\n"
            "А также\: шутки и приколы"
        )

        await bot.send_message(message.chat.id, text, parse_mode="MarkdownV2")

    @bot.message_handler()
    async def send_mem_image(message : Message) -> None:
        if (message.text.find("кот") != -1):
            random_image_path = random.choice(bot_data.cat_mem_paths)
            image = Image.open(random_image_path)

            await bot.send_photo(message.chat.id, image)
        elif (message.text.find("работ") != -1):
            pass
        elif (message.text.find("дет") != -1):
            pass
        elif (message.text.find("шутка") != -1 or message.text.find("прикол") != -1):    
            random_joke = random.choice(bot_data.jokes)

            await bot.send_message(message.chat.id, random_joke)
        else:
            text = "Такой категории не было найдено :("

            await bot.send_message(message.chat.id, text)


from pathlib import Path
from telebot.types import Message

def get_full_name(message : Message) -> str:
    user = message.from_user
    full_name = user.first_name + user.last_name if user.last_name != None else user.first_name

    return full_name

def get_sulution_dir():
    return Path(__file__).resolve().parent.parent

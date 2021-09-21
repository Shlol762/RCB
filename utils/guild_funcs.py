from discord.ext.commands import Bot
from discord import Message
import json


async def prefix(bot: Bot, message: Message) -> str:
    with open("C:/Users/Shlok/RCB/json/prefixes.json", "r") as f:
        prefixes = json.load(f)
    id: str = str(message.guild.id) if message.guild else "DM"
    return prefixes[id]

from discord.ext.commands import Bot
from discord import Message
import json
import os, re

PATH = re.search(r"C:[/\\]Users[/\\].+[/\\](RCB(-Live-Version)?)+", os.path.dirname(os.path.realpath(__file__))).group().replace('\\', '/')


async def prefix(bot: Bot, message: Message) -> str:
    with open(PATH + "/json/prefixes.json", "r") as f:
        prefixes = json.load(f)
    id: str = str(message.guild.id) if message.guild else "DM"
    return prefixes[id]

import json
from discord.ext.commands import Cog, Context, Bot
from discord import Guild, Message
from Cogs import PATH, farewell, greeting


class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.name = 'None'

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        with open(PATH + "/json/prefixes.json", "w") as f:
            prefixes = json.load(f)
            prefixes[str(guild.id)] = "!"
            json.dump(prefixes, f)

    @Cog.listener()
    async def on_message(self, message: Message):
        ctx = await self.bot.get_context(message)
        if message.author != self.bot.user:
            await farewell(ctx)
            await greeting(ctx)


async def setup(bot: Bot):
    await bot.add_cog(Events(bot))

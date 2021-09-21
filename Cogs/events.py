from discord.ext.commands import Cog, Context, Bot
from discord import Guild
from Cogs import PATH


class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.name = 'None'

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        with open(PATH + "/json/prefixes.json", "w") as f:
            pass
        pass



def setup(bot: Bot):
    bot.add_cog(Events(bot))

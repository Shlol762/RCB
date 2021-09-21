import discord
from discord.ext import commands
from utils import prefix


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True,
                   )

@bot.command(name="Ping")
async def ping(ctx: commands.Context):
    await ctx.reply(bot.latency)


bot.run()

import discord
from discord.ext import commands
from utils import prefix

retry = 0
while retry < 5:
    token = input("Specify token file path ")
    try:
        with open(token) as f:
            token = f.read()
    except FileNotFoundError:
        pass
    else:
        break
    retry+=1



intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True,
                   )

@bot.command(name="Ping")
async def ping(ctx: commands.Context):
    await ctx.reply(bot.latency)


bot.run(token)

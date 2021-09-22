import discord, os
from discord.ext import commands
from utils import prefix, PATH

retry = 0
while retry < 5:
    token = input("Specify token file path ")
    if token == '':
        token = "C:/Users/iamaa/Downloads/disc_bot_code.txt" if "iamaa" in PATH \
            else "C:/Users/Shlok/bot_stuff/token1.txt"
    try:
        with open(token) as f:
            token = f.read()
    except FileNotFoundError:
        pass
    else:
        break
    retry += 1


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)


for cog in os.listdir(PATH + "/Cogs"):
    if cog.endswith(".py") and cog != '__init__.py':
        bot.load_extension(f'Cogs.{cog[:-3]}')


@bot.command(name="Ping")
async def ping(ctx: commands.Context):
    await ctx.reply(bot.latency)

@bot.command(name="joke")
async def joke(ctx: commands.Context):
    await ctx.reply(ctx.author.mention)

bot.run(token)

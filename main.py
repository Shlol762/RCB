import discord, os
from discord.ext import commands
from utils import prefix, PATH
import random

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



@bot.command(name="toss")
async def toss(ctx: commands.Context):
    await ctx.reply(random.choice(["tails", "heads"]))


@bot.command(name="8ball")
async def ball(ctx: commands.Context):
    embed = discord.Embed(title="8ball", description=random.choice(["Yes.", "No.", "Maybe.", "Probably.", "Probably not.", "I'm not sure, try again.", "Doubtful.", "Definitely.", "Definitely not."]), colour=discord.Colour.random())
    await ctx.reply(embed=embed)


@bot.command(name="dice")
async def dice(ctx: commands.Context):
    await ctx.reply(random.randint(1,6))


bot.run(token)

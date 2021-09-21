import discord
from discord.ext import commands
from utils import prefix

retry = 0
while retry < 5:
    token = input("Specify token file path ")
    if token == '':
        token = "C:\\Users\\iamaa\\Downloads\\disc_bot_code.txt"
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

@bot.command(name="Hello")
async def hello(ctx: commands.Context):
    await ctx.reply("Hi there!")

@bot.command(name="Good_morning")
async def hello(ctx: commands.Context):
    await ctx.reply("Good morning!")

@bot.command(name="Bye")
async def hello(ctx: commands.Context):
    await ctx.reply("Byeee! Take care!")

bot.run(token)

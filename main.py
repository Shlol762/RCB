import discord, os
from discord.ext import commands
from utils import prefix, PATH
import random

retry = 0
while retry < 5:
    token = input("Aaroh or Shlok? ").lower()
    token = "C:/Users/iamaa/Downloads/disc_bot_code.txt" if "aaroh" in token\
        else "C:/Users/Shlok/bot_stuff/safe_docs/token1.txt"

    try:
        with open(token) as f:
            token = f.read()
            break
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
    await ctx.reply(random.choice(["Yes.", "No.", "Maybe.", "Probably.", "Probably not.", "I'm not sure, try again.", "Doubtful.", "Definitely.", "Definitely not."]))


@bot.command(name="dice")
async def dice(ctx: commands.Context):
    await ctx.reply(random.randint(1,6))


@bot.command(name="iplteams")
async def iplteams(ctx: commands.Context):
    await ctx.reply("\n".join(['MI',
                     'CSK',
                     'KKR',
                     'SRH',
                     'RR',
                     'RCB',
                     'DC',
                     'PBKS']))


@bot.command(name="iplstats")
async def iplstats(ctx: commands.Context):
    await ctx.reply("\n".join(['Most runs: Virat Kohli',
                    'Most wickets: Lasith Malinga',
                    'Most sixes: Chris Gayle',
                    'Best economy: Rashid Khan',
                    'Most fours: Shikhar Dhawan',
                    'Most dots: Harbhajan Singh']))


@bot.command(name="iplwinners")
async def iplwinners(ctx: commands.Context):
    await ctx.reply("\n".join(['2008: Rajasthan Royals',
                               '2009: Deccan Chargers',
                               '2010: Chennai Super Kings',
                               '2011: Chennai Super Kings',
                               '2012: Kolkata Knight Riders',
                               '2013: Mumbai Indians',
                               '2014: Kolkata Knight Riders',
                               '2015: Mumbai Indians',
                               '2016: Sunrisers Hyderabad',
                               '2017: Mumbai Indians',
                               '2018: Chennai Super Kings',
                               '2019: Mumbai Indians',
                               '2020: Mumbai Indians']))

@bot.command(name="pingus")
async def pingus(ctx: commands.Context):
    await ctx.reply("@everyone")



bot.run(token)

import datetime
import discord, os
from discord.ext import commands
from utils import prefix, PATH, IPLT20
import random
from asyncio import get_event_loop as get_loop
import logging


log_level = logging.INFO
log_formatter = discord.utils._ColourFormatter()
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)

log = logging.getLogger(__name__)
log.addHandler(log_handler)
log.setLevel(log_level)

log.info('Logging has been set up')


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
    retry += 1

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)

for cog in os.listdir(PATH + "/Cogs"):
    if cog.endswith(".py") and cog != '__init__.py':
        get_loop().run_until_complete(bot.load_extension(f'Cogs.{cog[:-3]}'))


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


@bot.command(name="pointstable", aliases=['ptstbl'])
async def _points_table(ctx: commands.Context, year: int = datetime.date.today().year):
    ipl = IPLT20()
    table = await ipl.points_table(year)
    head, body = table.to_str()

    await ctx.reply(f"```less\n{head}``````nim\n{body}```")



bot.run(token, log_handler=log_handler, log_formatter=log_formatter, log_level=log_level, root_logger = True)

from discord.ext.commands import Context
import re


async def greeting(ctx: Context):
    if re.search(r'^\b(hi|hello|hey)\b$', ctx.message.content.lower()):
        await ctx.reply(f"Hello {ctx.author.mention}!")


async def farewell(ctx: Context):
    if re.search(r'^\b(bye|(see|c) ya (later)?)\b$', ctx.message.content.lower()):
        await ctx.reply(f"Bye {ctx.author.mention}! Come back soon!")

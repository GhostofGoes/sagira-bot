from datetime import datetime

from discord import Colour, Embed
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context
from loguru import logger


class ScheduleCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx: Context):
        logger.info(f"Command: {ctx.command}\t{ctx.author.nick}")
        embed = Embed(colour=Colour.gold())
        embed.title = "some title"
        embed.description = "Howdy there I'm just a description"
        embed.timestamp = datetime.utcnow()
        embed.set_author(name="author-name")
        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(ScheduleCog(bot))

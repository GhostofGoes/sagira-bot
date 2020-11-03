from datetime import datetime
import discord
from discord import Colour, Embed
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context

from loguru import logger

raid_letters = ["🇨",
                "⏮️",
                "⏭️",
                "🇸",
                "😋"
                ]


class ScheduleCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx):

        embed = Embed(
            title="Raid",
            description='Choose What Raid you like to do',
            colour=Colour.dark_blue()
        )

        fields = [("Raids", "\n".join([f"{raid_letters[idx]}" for idx, raid in enumerate(raid_letters)]), False),
                  ("Instructions", "React to choose raid", False)
                  ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_thumbnail(url="https://www.destinypedia.com/images/thumb/8/89/Raid.jpg/250px-Raid.jpg",)

        message = await ctx.send(embed=embed)

        for var in raid_letters:
            await message.add_reaction(emoji=f"{var}")


def setup(bot) -> None:
    bot.add_cog(ScheduleCog(bot))

import discord
from discord.ext import commands


# TODO: for all commands, accept a user_id parameter
#   If not specified and user is registered, then we use the registered user's id
#   If not specified and NOT registered, user is prompted to register or provide an ID
#   If specified, use as the ID (How do we handle platforms? is a ID universal?)


class RaidReportCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="raidreport", aliases=("rr",))
    async def raidreport(self, ctx: commands.Context, user_id: str) -> None:
        """Raid summary."""

        # add argument to display legacy raids as well (stuff that's been vaulted)
        #   if enabled, also include legacy raid stats in overall stat calculations

        # TODO: resolve destiny user id to a name
        #   also need to handle names with spaces

        """
        Embed includes:
            Discord user's avatar as the embed thumbnail?
            Each raid (/w name + image of raid):
                # of full clears
                fastest time
                date of last clear
                kills
                deaths
                badges (as images?): flawless, week1, day1, solo, duo, trio, combos of these
            user's overall full clears count
            user's overall full clears rank
            user's overall clear count (full + checkpointed)
            average full clear time across all raids
            date of first raid ever attempted (include legacy)
            date of first raid ever completed (include legacy)
            date of latest raid completion (any raid)
            date of latest raid attempt (any raid)
        """

        embed = discord.Embed(
            title=f"insert_destiny_name ({ctx.message.author.display_name})",
            description="",
            colour=discord.Colour.green()
        )
        # raid.report will auto-correct a name on "/pc" to proper URL...so whatevs
        embed.add_field(
            name="Reports",
            value=f"[raid.report](https://raid.report/pc/{user_id})\n"
                  f"[dungeon.report](https://dungeon.report/pc/{user_id})",
            inline=False
        )
        embed.add_field(
            name="Join code",
            value=f"`/join {user_id}`",
            inline=False
        )
        # embed.set_thumbnail(url="https://i.imgur.com/ghrkNtC.png")
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RaidReportCog(bot))

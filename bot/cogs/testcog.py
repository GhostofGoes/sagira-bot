import discord
from discord import app_commands
from discord.ext import commands

from bot.constants import Config


# from discord import ui
# class Questionnaire(ui.Modal, title='Questionnaire Response'):
#     name = ui.TextInput(label='Name')
#     answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

#     async def on_submit(self, interaction: discord.Interaction):
#         await interaction.response.send_message(f'Thanks for your response, {self.name}!')


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="testcommand")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def testcommand(self, interaction: discord.Interaction) -> None:
        """some description"""
        await interaction.response.send_message("here's some test output")

    @app_commands.command(name="modaltest")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def modaltest(self, interaction: discord.Interaction) -> None:
        """some modal test lol"""
        await interaction.response.send_message("here's some test output")


async def setup(bot) -> None:
    await bot.add_cog(TestCog(bot))

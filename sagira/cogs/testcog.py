import discord
from discord import app_commands
from discord.ext import commands
from discord import ui

from sagira.constants import Config


class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)
    # question = ui.Select(options=[
    #     discord.SelectOption(
    #         label="opt1",
    #         value="val1",
    #         description="description1"
    #     )
    # ])

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Responses",
            description="",
            colour=discord.Colour.green()
        )
        embed.add_field(
            name="Name",
            value=self.name,
            inline=True
        )
        embed.add_field(
            name="Answer",
            value=self.answer,
            inline=True
        )
        await interaction.response.send_message(f'name={self.name}, answer={self.answer}', embed=embed)


class EditModal(ui.Modal, title='Edit raid'):
    name = ui.TextInput(label='NewName')
    answer = ui.TextInput(label='NewAnswer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Responses",
            description="",
            colour=discord.Colour.green()
        )
        embed.add_field(
            name="Name",
            value=self.name,
            inline=True
        )
        embed.add_field(
            name="Answer",
            value=self.answer,
            inline=True
        )
        await interaction.response.edit_message(content=f'new_name={self.name}, new_answer={self.answer}', embed=embed)


class EditButton(ui.Button):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EditModal())


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="testcommand")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def testcommand(self, interaction: discord.Interaction) -> None:
        """some description"""
        embed = discord.Embed(
            title="some title",
            description="",
            colour=discord.Colour.green()
        )
        view = ui.View()
        view.add_item(ui.Button(
            style=discord.ButtonStyle.primary,
            label="Join",
        ))
        view.add_item(ui.Button(
            style=discord.ButtonStyle.secondary,
            label="Leave",
        ))
        # view.add_item(ui.Button(
        #     style=discord.ButtonStyle.link,  # TODO: can this take a URL?
        #     label="Alternate",
        # ))
        view.add_item(EditButton(
            style=discord.ButtonStyle.danger,
            label="Edit"
        ))
        await interaction.response.send_message("here's some test output", embed=embed, view=view)

    @app_commands.command(name="modaltest")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def modaltest(self, interaction: discord.Interaction) -> None:
        """some modal test lol"""
        await interaction.response.send_modal(Questionnaire())

    @app_commands.command(name="selecttest")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def selecttest(self, interaction: discord.Interaction) -> None:
        """some select test lol"""
        modal = Questionnaire()
        # select = ui.Select()
        # select.add_option(
        #     label="opt1",
        #     value="val1",
        #     description="description1"
        # )
        # modal.add_item(select)
        await interaction.response.send_modal(modal)


async def setup(bot) -> None:
    await bot.add_cog(TestCog(bot))

from cgitb import text
import discord
from discord import SelectOption, app_commands
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
            title="",
            description="",
            colour=discord.Colour.blue()
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
        view = ui.View()
        view.add_item(JoinButton(
            style=discord.ButtonStyle.primary,
            label="Join",
        ))
        view.add_item(ui.Button(
            style=discord.ButtonStyle.danger,
            label="Leave",
        ))
        view.add_item(ui.Button(
            style=discord.ButtonStyle.primary,  # TODO: can this take a URL?
            label="Alternate",
        ))
        view.add_item(EditButton(
            style=discord.ButtonStyle.danger,
            label="Edit"
        ))
        view.add_item(ui.Select(
            custom_id="select-menu",
            placeholder='stuf',
            min_values=1,
            max_values=2,
            options=[
                SelectOption(label="option 1", value="option 1"),
                SelectOption(label="option 2", value="option 2")
            ]

        ))
        embed.set_footer(text= f"Author: {interaction.user.name}")
        embed.set_thumbnail(url="https://www.destinypedia.com/images/thumb/8/89/Raid.jpg/250px-Raid.jpg",)
        await interaction.response.send_message(embed=embed, view=view,)


class EditModal(ui.Modal, title='Edit raid'):
    name = ui.TextInput(label='NewName')
    answer = ui.TextInput(label='NewAnswer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Responses",
            description="",
            colour=discord.Colour.blue()
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
        embed.set_footer(text= f"Author: {interaction.user.name}") #todo edited by instead of author while also preserving original author
        embed.set_thumbnail(url="https://www.destinypedia.com/images/thumb/8/89/Raid.jpg/250px-Raid.jpg",)
        await interaction.response.edit_message(embed=embed)

class EditButton(ui.Button):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EditModal())

class JoinModal(ui.Modal,title='g'):
     name = ui.TextInput(label='NewName') # do i need this
     
     async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed()
        embed.add_field(
            name="Name",
            value=self.name,
            inline=True
        )
        await interaction.response.edit_message(embed=embed)




class JoinButton(ui.Button):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(JoinModal())



class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # @app_commands.command(name="make_event")
    # @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    # async def testcommand(self, interaction: discord.Interaction) -> None:
    #     """some description"""
        
    #     embed = discord.Embed(
    #         title="some title",
    #         description="",
    #         colour=discord.Colour.blue()
    #     )
    #     view = ui.View()
    #     view.add_item(ui.Button(
    #         style=discord.ButtonStyle.primary,
    #         label="Join",
    #     ))
    #     view.add_item(ui.Button(
    #         style=discord.ButtonStyle.danger,
    #         label="Leave",
    #     ))
    #     view.add_item(ui.Button(
    #         style=discord.ButtonStyle.primary,  # TODO: can this take a URL?
    #         label="Alternate",
    #     ))
    #     view.add_item(EditButton(
    #         style=discord.ButtonStyle.danger,
    #         label="Edit"
    #     ))
    #     embed.set_thumbnail(url="https://www.destinypedia.com/images/thumb/8/89/Raid.jpg/250px-Raid.jpg",)
    #     await interaction.response.send_message(embed=embed, view=view)

    @app_commands.command(name="modaltest")
    @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    async def modaltest(self, interaction: discord.Interaction) -> None:
        """some modal test lol"""
        await interaction.response.send_modal(Questionnaire())

    # @app_commands.command(name="selecttest")
    # @app_commands.guilds(discord.Object(id=Config.discord_guild_id))
    # async def selecttest(self, interaction: discord.Interaction) -> None:
    #     """some select test lol"""
    #     modal = Questionnaire()
    #     # select = ui.Select()
    #     # select.add_option(
    #     #     label="opt1",
    #     #     value="val1",
    #     #     description="description1"
    #     # )
    #     # modal.add_item(select)
    #     #await interaction.response.send_modal(modal)


async def setup(bot) -> None:
    await bot.add_cog(TestCog(bot))

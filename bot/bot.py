import discord
from discord.ext.commands import Bot
from loguru import logger

from bot.constants import Config
from bot.utils import walk_cogs


class SagiraBot(Bot):
    async def setup_hook(self) -> None:
        # Import all cogs
        logger.info("Loading cogs...")
        for cog in walk_cogs():
            logger.info(f"Loading cog: {cog}")
            await self.load_extension(cog)
        logger.info("Finished loading cogs")

        logger.info("Syncing bot command tree with Discord...")
        await self.tree.sync(guild=discord.Object(Config.discord_guild_id))
        logger.info("Finished syncing bot command tree with Discord")

        logger.info("Finished bot setup, Sagira is ready to go!")

import discord
from discord.ext.commands import Bot
from elasticsearch import AsyncElasticsearch
from loguru import logger

from sagira.constants import Config
from sagira.utils import COGS


class SagiraBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elastic = AsyncElasticsearch(Config.elastic_host)

    async def setup_hook(self) -> None:
        # Import all cogs
        logger.info("Loading cogs...")
        for cog in COGS:
            logger.info(f"Loading cog: {cog}")
            await self.load_extension(cog)
        logger.info("Finished loading cogs")

        logger.info("Syncing bot command tree with Discord...")
        await self.tree.sync(guild=discord.Object(Config.discord_guild_id))
        logger.info("Finished syncing bot command tree with Discord")

        logger.info("Finished bot setup, Sagira is ready to go!")

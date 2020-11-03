import discord
from loguru import logger

from bot.bot import SagiraBot
from bot.cogs.schedule import ScheduleCog
from bot.constants import Config

# TODO
#   * https://github.com/MagicStack/uvloop


logger.info(f"Creating bot instance (prefix: {Config.prefix})")
sagira_bot = SagiraBot(
    command_prefix=Config.prefix,
    activity=discord.Game(name=f"Help: {Config.prefix}help")
)

logger.info("Adding cog: ScheduleCog")
sagira_bot.add_cog(ScheduleCog(sagira_bot))

logger.info("Starting bot...")
sagira_bot.run(Config.token)

import discord
from loguru import logger

from bot.bot import SagiraBot
from bot.cogs.schedule import ScheduleCog
from bot.constants import Config
from . import __version__

# TODO
#   * https://github.com/MagicStack/uvloop

logger.info(
    f"Initializing Sagira\n"
    f"Version: {__version__}\n"
    f"Prefix: {Config.prefix}\n"
    f"DEBUG: {Config.debug}"
)
sagira_bot = SagiraBot(
    command_prefix=Config.prefix,
    activity=discord.Game(name=f"Help: {Config.prefix}help")
)

logger.info("Adding cog: ScheduleCog")
sagira_bot.add_cog(ScheduleCog(sagira_bot))

logger.info(f"Running Sagira v{__version__}")
sagira_bot.run(Config.token)

import discord
from loguru import logger

from bot.utils import walk_cogs
from bot.bot import SagiraBot
from bot.cogs.raid_report import RaidReportCog
from bot.cogs.schedule import ScheduleCog
from bot.constants import Config
from . import __version__

# Faster asyncio loop (not available on Windows)
# https://github.com/MagicStack/uvloop
try:
    import uvloop
    logger.info("Using uvloop for asyncio loop")
    uvloop.install()
except ImportError:
    logger.info("Using vanilla asyncio loop")

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


# Add all cogs
for cog in walk_cogs():
    logger.info(f"Adding cog: {cog.__name__}")
    sagira_bot.add_cog(cog(sagira_bot))
# cogs = [ScheduleCog, RaidReportCog]
# for cog in cogs:
#     logger.info(f"Adding cog: {cog.__name__}")
#     sagira_bot.add_cog(cog(sagira_bot))


logger.info(f"Running Sagira v{__version__}")
sagira_bot.run(Config.token)


# import os
# import asyncio
# import motor.motor_asyncio
# host = os.environ["MONGO_HOSTNAME"]
# user = os.environ["MONGO_USERNAME"]
# pswd = os.environ["MONGO_PASSWORD"]
# port = os.environ["MONGO_PORT"]
# client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{user}:{pswd}@{host}:{port}")
# db = client["sagiradb"]
#
# col = db["schedules"]
#
# async def insert():
#     test_doc = {"hi": "hello", "one": 1}
#     result = await col.insert_one(test_doc)
#     logger.info(result)
#
# async def find():
#     cursor = col.find_one()
#     logger.info(cursor)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(insert())
# loop.run_until_complete(find())

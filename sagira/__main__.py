#!/usr/bin/env python3

import asyncio
import json

import aiobungie
import discord
from loguru import logger

from sagira import __version__
from sagira.bot import SagiraBot
from sagira.constants import Config, Vars

# TODO: configure logging levels based on Config.debug


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
    f"Discord version: {discord.__version__}\n"
    f"Sagira version: {__version__}\n"
    f"Debug: {Config.debug}"
)
sagira_bot = SagiraBot(
    command_prefix="!",
    activity=discord.Game(name="Help: !help"),
    application_id=Config.discord_app_id,
    intents=discord.Intents.all(),
)


# Discord.py 2.0 added async support
#   https://stackoverflow.com/a/71504716
#   https://gist.github.com/Rapptz/6706e1c8f23ac27c98cee4dd985c8120
async def main() -> None:
    # Connect to Bungie API
    client = aiobungie.Client(Config.bungie_api_key)

    # clan = await client.fetch_clan("Literally The Coolest")
    # members = await clan.fetch_members()
    # # Filter the results to return only steam members from the clan.
    # for member in members.filter(lambda m: m.type is aiobungie.MembershipType.STEAM):
    #     # Get the profile for this clan member.
    #     profile = await member.fetch_self_profile(
    #         components=[aiobungie.ComponentType.CHARACTERS]
    #     )
    #     print(profile.characters)

    # Download Manifest file (~334MB JSON file)
    # (there's also a SQLite version that may be slightly smaller)
    # This file has all of the item definitions for everything in the game
    # short version: the API returns references to items as hashes
    # The manifest is used to lookup the hashes and get actual information,
    # such as the item name, description, and icon.
    # Further reading:
    # https://github.com/Bungie-net/api/wiki/Obtaining-Destiny-Definitions-%22The-Manifest%22
    # Cache manifest file, only download if there's a newer version
    if Vars.manifest_version_path.is_file():
        logger.info(f"Reading cached manifest version from {Vars.manifest_version_path}")
        Vars.manifest_version = Vars.manifest_version_path.read_text()
    latest_manifest_version = await client.rest.fetch_manifest_version()
    logger.info(f"Latest manifest version: {latest_manifest_version}")
    logger.info(f"Current manifest version: {Vars.manifest_version}")
    if latest_manifest_version != Vars.manifest_version:
        logger.info(
            f"Latest manifest version '{latest_manifest_version}' does not match cached "
            f"manifest version '{Vars.manifest_version}' or the manifest file hasn't been "
            f"downloaded yet, downloading a fresh manifest file from Bungie..."
        )
        await client.rest.download_json_manifest()
        logger.info("Finished downloading updated manifest file, writing version to cache file...")
        Vars.manifest_version_path.write_text(latest_manifest_version)
    Vars.manifest_version = latest_manifest_version
    logger.info(f"Manifest path: {Vars.manifest_json_path}")

    # Read the manifest into a dict
    Vars.manifest = json.loads(Vars.manifest_json_path.read_text())
    # print(list(Vars.manifest.keys()))

    # Start the bot
    async with sagira_bot:
        logger.info(f"Running Sagira v{__version__}")
        await sagira_bot.start(Config.discord_token)


asyncio.run(main())

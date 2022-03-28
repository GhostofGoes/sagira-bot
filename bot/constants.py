from distutils.util import strtobool
from os import environ
from typing import NamedTuple

# If testing locally (not in Docker), load environment variables from .env file
try:
    import dotenv
    dotenv.load_dotenv()
except ModuleNotFoundError:
    pass


class Config(NamedTuple):
    prefix = environ.get("COMMAND_PREFIX", "!")
    discord_token = environ["DISCORD_TOKEN"]
    debug = strtobool(environ.get("DEBUG", "false").lower())
    bungie_api_key = environ.get("BUNGIE_API_KEY", "")
    bungie_oauth_client_id = environ.get("BUNGIE_OAUTH_CLIENT_ID", "")
    bungie_oauth_client_secret = environ.get("BUNGIE_OAUTH_CLIENT_SECRET", "")

class Colours:
    blue: int = 0x0279fd
    bright_green: int = 0x01d277
    dark_green: int = 0x1f8b4c
    orange: int = 0xe67e22
    pink: int = 0xcf84e0
    purple: int = 0xb734eb
    soft_green: int = 0x68c290
    soft_orange: int = 0xf9cb54
    soft_red: int = 0xcd6d6d
    yellow: int = 0xf9f586


class Links:
    github_url = "https://github.com/GhostofGoes/sagira-bot"
    github_avatar_url = "https://avatars1.githubusercontent.com/u/9919"
    sagira_wiki = "https://www.destinypedia.com/Sagira"


# https://en.wikiquote.org/wiki/Destiny_2
ERROR_REPLIES = [
    "Ow!",
    "Yeah, that wasn't supposed to happen...",
]

NEGATIVE_REPLIES = [
    "Need help? Again?",
    "Ominous rocks, killer robots, people in mortal danger... seriously, aren't you tired of this?",
    "I'm sorry Dave, I'm afraid I can't do that.",
]

POSITIVE_REPLIES = [
    "You're welcome.",
    "Great!",
    "That worked",
]

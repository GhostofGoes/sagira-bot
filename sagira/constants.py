from distutils.util import strtobool
from os import environ
from pathlib import Path
from typing import List

# If testing locally (not in Docker), load environment variables from .env file
try:
    import dotenv
    dotenv.load_dotenv()
except ModuleNotFoundError:
    pass


class Config:
    debug: bool = bool(strtobool(environ.get("DEBUG", "false").lower()))
    discord_token: str = environ["DISCORD_TOKEN"]
    discord_app_id: str = environ["DISCORD_APP_ID"]
    discord_public_key: str = environ["DISCORD_PUBLIC_KEY"]
    discord_guild_id: str = environ["DISCORD_GUILD_ID"]
    bungie_api_key: str = environ.get("BUNGIE_API_KEY", "")
    bungie_oauth_client_id: str = environ.get("BUNGIE_OAUTH_CLIENT_ID", "")
    bungie_oauth_client_secret: str = environ.get("BUNGIE_OAUTH_CLIENT_SECRET", "")
    elastic_host: str = environ.get("ELASTIC_HOST", "http://elasticsearch:9200")
    elastic_password: str = environ["ELASTIC_PASSWORD"]
    log_dir: Path = Path(environ.get("LOG_DIR", "./logs")).resolve()
    data_dir: Path = Path(environ.get("DATA_DIR", "./data")).resolve()
    manifest_json_path: Path = data_dir / "manifest.json"
    manifest_version_path: Path = data_dir / "manifest_version.txt"


class Vars:
    manifest_version: str = ""
    manifest: dict = {}


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


class Consts:
    github_url: str = "https://github.com/GhostofGoes/sagira-bot"
    github_avatar_url: str = "https://avatars1.githubusercontent.com/u/9919"
    sagira_wiki: str = "https://www.destinypedia.com/Sagira"


# https://en.wikiquote.org/wiki/Destiny_2
ERROR_REPLIES: List[str] = [
    "Ow!",
    "Yeah, that wasn't supposed to happen...",
]

NEGATIVE_REPLIES: List[str] = [
    "Need help? Again?",
    "Ominous rocks, killer robots, people in mortal danger... seriously, aren't you tired of this?",  # noqa: E501
    "I'm sorry Dave, I'm afraid I can't do that.",
]

POSITIVE_REPLIES: List[str] = [
    "You're welcome.",
    "Great!",
    "That worked",
]

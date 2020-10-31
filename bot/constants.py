from distutils.util import strtobool
from os import environ
from typing import NamedTuple


# Note: pipenv automatically loads variables from .env
# when using "pipenv run start"
class Config(NamedTuple):
    prefix = environ.get("PREFIX", "?")
    token = environ["SAGIRA_TOKEN"]
    debug = strtobool(environ.get("SAGIRA_TOKEN_DEBUG", "false").lower())
    github_url = "https://github.com/GhostofGoes/sagira-bot"

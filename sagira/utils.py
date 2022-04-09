import importlib
import inspect
import pkgutil
from collections.abc import Iterator
from typing import NoReturn

from discord.ext.commands import Context

from sagira import cogs


# SOURCE: python-discord/sir-lancebot
def unqualify(name: str) -> str:
    """Return an unqualified name given a qualified module/package `name`."""
    return name.rsplit(".", maxsplit=1)[-1]


# SOURCE: python-discord/sir-lancebot
def walk_cogs() -> Iterator[str]:
    """Yield cog names from the bot.cogs subpackage."""

    def on_error(name: str) -> NoReturn:
        raise ImportError(name=name)  # pragma: no cover

    for module in pkgutil.walk_packages(cogs.__path__, f"{cogs.__name__}.", onerror=on_error):
        if unqualify(module.name).startswith("_"):
            # Ignore module/package names starting with an underscore.
            continue

        if module.ispkg:
            imported = importlib.import_module(module.name)
            if not inspect.isfunction(getattr(imported, "setup", None)):
                # If it lacks a setup function, it's not a cog.
                continue

        yield module.name

COGS = frozenset(walk_cogs())

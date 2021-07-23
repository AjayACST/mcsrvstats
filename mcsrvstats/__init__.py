"""Minecraft Server Stats Wrapper.

~~~~~~~~~~~~~~~~~~~
A wrapper for a collection of popular minecraft server stats.
:copyright: (c) 2021 Obsidion-Dev
:license: MIT, see LICENSE for more details.
"""
from .main import Client

__title__ = "mcsrvstats"
__author__ = "Obsidion-Dev"
__license__ = "MIT"
__copyright__ = "Copyright 2021 Obsidion-Dev"


try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.2.0"

__all__ = ["Client"]

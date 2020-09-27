"""Minecraft Server Stats Wrapper.

~~~~~~~~~~~~~~~~~~~
A wrapper for a collection of popular minecraft server stats.
:copyright: (c) 2020 Darkflame72
:license: MIT, see LICENSE for more details.
"""

__title__ = "mcsrvstats"
__author__ = "Leon Bowie"
__license__ = "MIT"
__copyright__ = "Copyright 2020 Darkflame72"


try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


from collections import namedtuple


VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=0, minor=1, micro=1, releaselevel="alpha", serial=0)

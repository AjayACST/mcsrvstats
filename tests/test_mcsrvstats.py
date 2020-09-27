"""Main tests."""

from mcsrvstats import __version__


def test_version() -> None:
    """Mock version."""
    assert __version__ == "0.1.1"

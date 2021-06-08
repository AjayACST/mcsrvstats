"""Test for Universocraft."""
from mcsrvstats import Client

import pytest
from aioresponses import aioresponses

@pytest.mark.asyncio
async def test_universocraft(mcsrvstats_client: Client) -> None:
    """Test to check the universocraft function returns the correct data."""

    f = open("tests/html/test_universocraft.html", "r")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://stats.universocraft.com/stats.php?player=uBored",
            status=200,
            payload=html
        )

        client = mcsrvstats_client
        data = await client.universocraft("uBored")

        assert data.DestoryNexus.victories == 5
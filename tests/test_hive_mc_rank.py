"""Test for Hive Rank."""
from mcsrvstats import Client

import pytest
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_hive_rank(mcsrvstats_client: Client) -> None:
    """Test to check the hive_mc_rank function returns the correct data."""
    with aioresponses() as m:
        m.get(
            "http://api.hivemc.com/v1/player/Arrow_Plays",
            status=200,
            payload={
                "rankName": "Regular Hive Member",
            },
        )
        client = mcsrvstats_client
        data = await client.hive_mc_rank("Arrow_Plays")

        assert data.rank == "Regular Hive Member"

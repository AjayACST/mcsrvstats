"""Test for Hive Status."""
from mcsrvstats import Client

import pytest
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_hive_status(mcsrvstats_client: Client) -> None:
    """Test to check the hive_mc_status function returns the correct data."""
    with aioresponses() as m:
        m.get(
            "http://api.hivemc.com/v1/player/Arrow_Plays",
            status=200,
            payload={
                "status": {
                    "description": "Currently hibernating in",
                    "game": "the Land of Nods!",
                },
            },
        )
        client = mcsrvstats_client
        data = await client.hive_mc_status("Arrow_Plays")

        assert data.description == "Currently hibernating in"
        assert data.game == "the Land of Nods!"

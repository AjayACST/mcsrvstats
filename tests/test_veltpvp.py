"""Test for VeltPVP."""
import pytest
from aioresponses import aioresponses
from mcsrvstats import Client


@pytest.mark.asyncio
async def test_veltpvp(mcsrvstats_client: Client) -> None:
    """Test to check the veltpvp function returns the correct data."""

    f = open("tests/html/test_veltpvp.html")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://www.veltpvp.com/u/JOAKIM",
            status=200,
            body=html,
        )
        client = mcsrvstats_client
        data = await client.veltpvp("JOAKIM")

        assert data.rank == "Owner"
        assert data.lastSeen == "N/A"
        assert data.currentStatus == "N/A"
        assert data.firstJoined == "24/08/2017"
        assert data.timePlayed == "6 months played"
        assert data.monthlyViews == 11575

        assert data.HCF.Kills == 10
        assert data.HCF.Deaths == 1
        assert data.HCF.KDR == 10.0
        assert data.HCF.Lives == 0
        assert data.HCF.Playtime == "5 hours"

        assert data.Practice.Kills == 50
        assert data.Practice.Deaths == 3
        assert data.Practice.Wins == 0
        assert data.Practice.Losses == 0
        assert data.Practice.Fights == 0
        assert data.Practice.GlobalELO == 1000

        assert data.Soup.Kills == 0
        assert data.Soup.Deaths == 0
        assert data.Soup.HighestKillstreak == 0
        assert data.Soup.EventsWon == 0
        assert data.Soup.EventsLost == 0

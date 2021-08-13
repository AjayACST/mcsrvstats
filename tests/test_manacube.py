"""Test for Manaucbe."""
from datetime import datetime

import pytest
from aioresponses import aioresponses
from mcsrvstats import Client
from mcsrvstats import exceptions


@pytest.mark.asyncio
async def test_manacube(mcsrvstats_client: Client) -> None:
    """Test to check the manacube function returns the correct data."""
    with aioresponses() as m:
        m.get(
            "https://manacube.com/stats_data/fetch.php?username=_iTempo",
            status=200,
            payload={
                "exists": True,
                "level": "14",
                "rank": "default",
                "cubits": "61.87",
                "firstSeen": "2019-07-07 00:22:11",
                "lastSeen": "2021-01-20 01:07:32",
                "lastSeenAgo": "1 second ago",
                "parkour": {
                    "playtime": "15 hours",
                    "mana": "N/A",
                    "score": "0",
                    "courses": 0,
                },
                "aztec": {
                    "playtime": "3046 hours",
                    "mobKills": "0",
                    "mana": "150",
                    "money": "50",
                },
                "oasis": {
                    "playtime": "1 hours",
                    "mobKills": "0",
                    "mana": "185",
                    "money": "2000000051",
                },
                "islands": {
                    "playtime": "6244 hours",
                    "mobKills": "0",
                    "silver": "13950",
                    "money": "3188330000",
                },
                "survival": {
                    "playtime": "0 mins",
                    "mobKills": "0",
                    "money": "300",
                    "quests": "0",
                },
                "factions": {
                    "playtime": "N/A",
                    "kills": "N/A",
                    "mobkills": "N/A",
                    "money": "N/A",
                },
                "aether": {
                    "playtime": "N/A",
                    "miningLevel": "N/A",
                    "money": "N/A",
                    "rebirths": "N/A",
                },
                "atlas": {
                    "playtime": "N/A",
                    "miningLevel": "N/A",
                    "money": "N/A",
                    "rebirths": "N/A",
                },
                "creative": {
                    "playtime": "73 hours",
                    "blocksplaced": "0",
                    "blocksbroken": "0",
                },
                "kitpvp": {
                    "playtime": "7 mins",
                    "level": "0",
                    "money": "10",
                    "kills": "0",
                },
            },
        )
        client = mcsrvstats_client
        data = await client.manacube("_iTempo")

        assert data.exists
        assert data.level == 14
        assert data.rank == "default"
        assert data.cubits == 61.87
        assert data.firstseen == datetime.strptime(
            "2019-07-07 00:22:11", "%Y-%m-%d %H:%M:%S"
        )
        assert data.lastseen == datetime.strptime(
            "2021-01-20 01:07:32", "%Y-%m-%d %H:%M:%S"
        )
        assert data.lastseenago == "1 second ago"

        assert data.parkour.playtime == "15 hours"
        assert data.parkour.mana == 0
        assert data.parkour.score == 0
        assert data.parkour.courses == 0

        assert data.aztec.playtime == "3046 hours"
        assert data.aztec.mobkills == 0
        assert data.aztec.mana == 150
        assert data.aztec.money == 50

        assert data.oasis.playtime == "1 hours"
        assert data.oasis.mobkills == 0
        assert data.oasis.mana == 185
        assert data.oasis.money == 2000000051

        assert data.islands.playtime == "6244 hours"
        assert data.islands.mobkills == 0
        assert data.islands.silver == 13950
        assert data.islands.money == 3188330000

        assert data.survival.playtime == "0 mins"
        assert data.survival.mobkills == 0
        assert data.survival.money == 300
        assert data.survival.quests == 0

        assert data.factions.playtime == "No Time"
        assert data.factions.kills == 0
        assert data.factions.mobkills == 0
        assert data.factions.money == 0

        assert data.aether.playtime == "No Time"
        assert data.aether.mininglevel == 0
        assert data.aether.money == 0
        assert data.aether.rebirths == 0

        assert data.atlas.playtime == "No Time"
        assert data.atlas.mininglevel == 0
        assert data.atlas.money == 0
        assert data.atlas.rebirths == 0

        assert data.creative.playtime == "73 hours"
        assert data.creative.blocksplaced == 0
        assert data.creative.blocksbroken == 0

        assert data.kitpvp.playtime == "7 mins"
        assert data.kitpvp.level == 0
        assert data.kitpvp.money == 10
        assert data.kitpvp.kills == 0


@pytest.mark.asyncio
async def test_manacube_not_found(mcsrvstats_client: Client) -> None:
    """Checks manacube returns correct data when player is not found."""
    with aioresponses() as m:
        m.get(
            "https://manacube.com/stats_data/fetch.php?username=_iTempo",
            status=200,
            payload={
                "exists": False,
            },
        )

        client = mcsrvstats_client

        with pytest.raises(exceptions.exceptions.PlayerNotFoundError):
            await client.manacube("_iTempo")

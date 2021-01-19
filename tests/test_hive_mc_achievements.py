"""Test for Hive Achievements."""
import pytest
from aioresponses import aioresponses
from mcsrvstats import Client


@pytest.mark.asyncio
async def test_hive_achievements(mcsrvstats_client: Client) -> None:
    """Test to check the hive_mc_achievements returns the correct data."""
    with aioresponses() as m:
        m.get(
            "http://api.hivemc.com/v1/player/Arrow_Plays",
            status=200,
            payload={
                "achievements": {
                    "THESWARM": {
                        "progress": 1,
                        "unlockedAt": 1424896870,
                        "from": "1392af3c92104fcb803dd8bac6ba0577",
                        "game": "SurvivalGames",
                    },
                    "HUB": {"progress": 1, "unlockedAt": 1424897037},
                    "PLAY1": {"progress": 1, "unlockedAt": 1424898628},
                    "SPREDDIT": {"progress": 15, "unlockedAt": 0},
                    "SESSION3": {"progress": 1, "unlockedAt": 1431401290},
                    "PLAY24": {"progress": 1, "unlockedAt": 1431459402},
                    "FRIENDACCEPTINVITE": {"progress": 1, "unlockedAt": 1436219277},
                    "FRIEND1": {"progress": 1, "unlockedAt": 1436219277},
                    "JOIN1": {"progress": 1, "unlockedAt": 1487614875},
                    "JOIN2": {"progress": 1, "unlockedAt": 1499973774},
                    "PLAY168": {"progress": 1, "unlockedAt": 1505602303},
                    "PARTYACCEPT": {"progress": 1, "unlockedAt": 1516734331},
                    "JOIN3": {"progress": 1, "unlockedAt": 1520303897},
                    "JOIN4": {"progress": 1, "unlockedAt": 1571877414},
                }
            },
        )
        client = mcsrvstats_client
        data = await client.hive_mc_achievments("Arrow_Plays")

        assert len(data.all_achievements) == 14
        assert data.all_achievements[0] == "THESWARM"
        assert data.all_achievements[1] == "HUB"
        assert data.all_achievements[2] == "PLAY1"
        assert data.all_achievements[3] == "SPREDDIT"
        assert data.all_achievements[4] == "SESSION3"
        assert data.all_achievements[5] == "PLAY24"
        assert data.all_achievements[6] == "FRIENDACCEPTINVITE"
        assert data.all_achievements[7] == "FRIEND1"
        assert data.all_achievements[8] == "JOIN1"
        assert data.all_achievements[9] == "JOIN2"
        assert data.all_achievements[10] == "PLAY168"
        assert data.all_achievements[11] == "PARTYACCEPT"
        assert data.all_achievements[12] == "JOIN3"
        assert data.all_achievements[13] == "JOIN4"

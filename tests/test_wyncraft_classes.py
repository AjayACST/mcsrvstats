"""Test for wyncraft classes."""
import pytest
from aioresponses import aioresponses
from mcsrvstats import Client
from mcsrvstats import exceptions


@pytest.mark.asyncio
async def test_wyncraft_classes(mcsrvstats_client: Client) -> None:
    """Test to check the wyncraft classes function returns hte correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.wynncraft.com/v2/player/IceWarox/stats",
            status=200,
            payload={
                "kind": "wynncraft/player/IceWarox/stats",
                "code": 200,
                "timestamp": 1619819876728,
                "version": "2.1.0",
                "data": [
                    {
                        "classes": [
                            {
                                "name": "shaman",
                                "level": 1678,
                                "chestsFound": 970,
                                "logins": 9362,
                                "deaths": 789,
                                "discoveries": 895,
                                "eventsWon": 0,
                            },
                        ]
                    }
                ],
            },
        )
        client = mcsrvstats_client
        data = await client.wynncraft_classes("IceWarox")

        assert data.classes[0].class_name == "shaman"
        assert data.classes[0].class_level == 1678
        assert data.classes[0].class_chest == 970
        assert data.classes[0].class_logins == 9362
        assert data.classes[0].class_deaths == 789
        assert data.classes[0].class_discoveries == 895
        assert data.classes[0].class_events_won == 0


@pytest.mark.asyncio
async def test_wyncraft_classes_player_not_found(mcsrvstats_client: Client) -> None:
    """Test to check the wyncraft classes function returns the correct data when the player is not found."""

    with aioresponses() as m:
        m.get(
            "https://api.wynncraft.com/v2/player/IceWarox/stats",
            status=200,
            payload={
                "kind": "wynncraft/player/IceWarox/stats",
                "code": 400,
                "timestamp": 1619819876728,
                "version": "2.1.0",
            },
        )

        client = mcsrvstats_client

        with pytest.raises(exceptions.exceptions.PlayerNotFoundError):
            await client.wynncraft_classes("IceWarox")

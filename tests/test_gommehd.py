"""Test for GommeHD."""
import pytest
from aioresponses import aioresponses
from mcsrvstats import Client
from mcsrvstats import exceptions

@pytest.mark.asyncio
async def test_gommehd(mcsrvstats_client: Client) -> None:
    """Test to check the gommehd function returns the correct data."""
    f = open("tests/html/test_gommehd.html", "r")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://www.gommehd.net/player/index?playerName=jsn78",
            status=200,
            body=html,
        )

        client = mcsrvstats_client
        data = await client.gommehd("jsn78")

        assert data.TTT.wins == 117
        assert data.TTT.kills == 470
        assert data.TTT.karma == 6580
        assert data.TTT.deaths == 253

        assert data.BedWars.wins == 650
        assert data.BedWars.kills == 2183
        assert data.BedWars.games == 1118
        assert data.BedWars.BedsDestroyed == 1540
        assert data.BedWars.deaths == 471

        assert data.SkyWars.wins == 351
        assert data.SkyWars.kills == 1446
        assert data.SkyWars.deaths == 510

        assert data.SurvivalGames.wins == 3
        assert data.SurvivalGames.kills == 34
        assert data.SurvivalGames.deaths == 32
        assert data.SurvivalGames.points == 1280

        assert data.EnderGames.wins == 0
        assert data.EnderGames.kills == 4
        assert data.EnderGames.deaths == 7

        assert data.QuickSurvivalGames.wins == 7
        assert data.QuickSurvivalGames.kills == 119
        assert data.QuickSurvivalGames.deaths == 69
        assert data.QuickSurvivalGames.points == 3780

        assert data.Cores.wins == 199
        assert data.Cores.kills == 1465
        assert data.Cores.deaths == 771

        assert data.GunGame.kills == 2021

        assert data.SpeedUHC.wins == 1
        assert data.SpeedUHC.kills == 3
        assert data.SpeedUHC.deaths == 5
        assert data.SpeedUHC.points == 5

        assert data.MasterBuilders.wins == 0
        assert data.MasterBuilders.games == 12
        assert data.MasterBuilders.points == 135

        assert data.Cookies.wins == 3
        assert data.Cookies.cookies == 4581

        assert data.Hardcore.kills == 629
        assert data.Hardcore.deaths == 677


@pytest.mark.asyncio
async def test_gommehd_player_not_found(mcsrvstats_client: Client) -> None:
    """Checks gommehd returns correct data when the player is not found."""
    f = open("tests/html/test_gommehd_player_not_found.html", "r")
    html = f.read()

    with aioresponses() as m:
        m.get(
            "https://www.gommehd.net/player/index?playerName=jsn78",
            status=200,
            body=html,
        )

        client = mcsrvstats_client
        with pytest.raises(exceptions.exceptions.PlayerNotFoundError):
            await client.gommehd("jsn78")

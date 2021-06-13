"""Test for GommeHD."""

from mcsrvstats import Client

import pytest
from aioresponses import aioresponses

@pytest.mark.asyncio
async def test_gommehd(mcsrvstats_client: Client) -> None:
    """Test to check the gommehd function returns the correct data."""

    f = open("tests/html/test_gommehd.html", "r")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://www.gommehd.net/player/index?playerName=jsn78",
            status=200,
            body=html
        )

        client = mcsrvstats_client
        data = await client.gommehd("jsn78")

        assert data.TTT.Wins == 117
        assert data.TTT.Kills == 470
        assert data.TTT.Karma == 6580
        assert data.TTT.Deaths == 253
        
        assert data.BedWars.Wins == 650
        assert data.BedWars.Kills == 2183
        assert data.BedWars.Games == 1118
        assert data.BedWars.BedsDestroyed == 1540
        assert data.BedWars.Deaths == 471

        assert data.SkyWars.Wins == 351
        assert data.SkyWars.Kills ==1446
        assert data.SkyWars.Deaths == 510
        
        assert data.SurvivalGames.Wins == 3
        assert data.SurvivalGames.Kills == 34
        assert data.SurvivalGames.Deaths == 32
        assert data.SurvivalGames.Points == 1280
        
        assert data.EnderGames.Wins == 0
        assert data.EnderGames.Kills == 4
        assert data.EnderGames.Deaths == 7

        assert data.QuickSurvivalGames.Wins == 7
        assert data.QuickSurvivalGames.Kills == 119
        assert data.QuickSurvivalGames.Deaths == 69
        assert data.QuickSurvivalGames.Points == 3780

        assert data.Cores.Wins == 199
        assert data.Cores.Kills == 1465
        assert data.Cores.Deaths == 771

        assert data.GunGame.Kills == 2021

        assert data.SpeedUHC.Wins == 1
        assert data.SpeedUHC.Kills == 3
        assert data.SpeedUHC.Deaths == 5
        assert data.SpeedUHC.Points == 5

        assert data.MasterBuilders.Wins == 0
        assert data.MasterBuilders.Games == 12
        assert data.MasterBuilders.Points == 135

        assert data.Cookies.Wins == 3
        assert data.Cookies.Cookies == 4581

        assert data.Hardcore.Kills == 629
        assert data.Hardcore.Deaths == 677
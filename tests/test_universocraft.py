"""Test for Universocraft."""
import pytest
from aioresponses import aioresponses
from mcsrvstats import Client
from mcsrvstats import exceptions


@pytest.mark.asyncio
async def test_universocraft(mcsrvstats_client: Client) -> None:
    """Test to check the universocraft function returns the correct data."""
    f = open("tests/html/test_universocraft.html", "r")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://stats.universocraft.com/stats.php?player=uBored",
            status=200,
            body=html,
        )

        client = mcsrvstats_client
        data = await client.universocraft("uBored")

        assert data.DestoryNexus.victories == 5
        assert data.DestoryNexus.murders == 137
        assert data.DestoryNexus.archedmurders == 0
        assert data.DestoryNexus.deaths == 94
        assert data.DestoryNexus.damagenexus == 165
        assert data.DestoryNexus.nexusdestructions == 1
        assert data.DestoryNexus.blocksplaced == 226
        assert data.DestoryNexus.destroyedblocks == 824
        assert data.DestoryNexus.oresdestroyed == 322
        assert data.DestoryNexus.logsdestroyed == 36

        assert data.SkyWars.victories == 613
        assert data.SkyWars.murders == 3450
        assert data.SkyWars.deaths == 755
        assert data.SkyWars.blocksplaced == 39024
        assert data.SkyWars.destroyedblocks == 3091
        assert data.SkyWars.projectileslaunch == 14774
        assert data.SkyWars.impactedprojectiles == 3805

        assert data.LuckyWars.victories == 11005
        assert data.LuckyWars.murders == 50201
        assert data.LuckyWars.deaths == 5543
        assert data.LuckyWars.blocksplaced == 68201
        assert data.LuckyWars.destroyedblocks == 43670
        assert data.LuckyWars.projectileslaunch == 9333
        assert data.LuckyWars.impactedprojectiles == 4517

        assert data.EggWars.victories == 166
        assert data.EggWars.murders == 2188
        assert data.EggWars.brokeneggs == 303
        assert data.EggWars.deaths == 522
        assert data.EggWars.blocksplaced == 27216
        assert data.EggWars.destroyedblocks == 1701
        assert data.EggWars.projectileslaunch == 443
        assert data.EggWars.impactedprojectiles == 257

        assert data.BedWars.victories == 151
        assert data.BedWars.murders == 1896
        assert data.BedWars.finalmurders == 595
        assert data.BedWars.destroyedbeds == 268
        assert data.BedWars.deaths == 873
        assert data.BedWars.finaldeaths == 100
        assert data.BedWars.gamesplayed == 264

        assert data.TeamSkyWars.victories == 3354
        assert data.TeamSkyWars.murders == 31247
        assert data.TeamSkyWars.deaths == 2327
        assert data.TeamSkyWars.blocksplaced == 270382
        assert data.TeamSkyWars.destroyedblocks == 22574
        assert data.TeamSkyWars.projectileslaunch == 64955
        assert data.TeamSkyWars.impactedprojectiles == 17871

        assert data.SpeedBuilders.victories == 15
        assert data.SpeedBuilders.lost == 27
        assert data.SpeedBuilders.perfectconstructions == 457

        assert data.BuildBattle.victories == 1
        assert data.BuildBattle.gamesplayed == 31
        assert data.BuildBattle.score == 79

        assert data.EscapeBeast.totalvictories == 95
        assert data.EscapeBeast.victoriesrunner == 91
        assert data.EscapeBeast.victoriesbeast == 4
        assert data.EscapeBeast.murdersrunner == 42
        assert data.EscapeBeast.murdersbeast == 42

        assert data.PartyGames.victories == 112
        assert data.PartyGames.murders == 3273
        assert data.PartyGames.deaths == 1484
        assert data.PartyGames.gamesplayed == 182

        assert data.HungerGames.victories == 410
        assert data.HungerGames.murders == 0
        assert data.HungerGames.deaths == 277

        assert data.SkyPit.level == 42
        assert data.SkyPit.unicoins == 609312
        assert data.SkyPit.assists == 32349
        assert data.SkyPit.murders == 67097
        assert data.SkyPit.deaths == 6553

        assert data.ArenaPVP.victories == 630
        assert data.ArenaPVP.murders == 756
        assert data.ArenaPVP.lost == 261

        assert data.UHC.victories == 9
        assert data.UHC.lost == 22
        assert data.UHC.gamesplayed == 37
        assert data.UHC.murders == 94
        assert data.UHC.deaths == 22

        assert data.MurderMystery.victories == 56
        assert data.MurderMystery.lost == 43
        assert data.MurderMystery.murders == 82
        assert data.MurderMystery.deaths == 43

        assert data.CaptureWool.score == 0
        assert data.CaptureWool.murders == 0
        assert data.CaptureWool.archedmurders == 0
        assert data.CaptureWool.maxarchdistance == 0
        assert data.CaptureWool.woolplaced == 0


@pytest.mark.asyncio
async def test_universocraft_player_not_found(mcsrvstats_client: Client) -> None:
    """Checks universocraft returns correct data when player is not found."""
    f = open("tests/html/test_universocraft_player_not_found.html")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://stats.universocraft.com/stats.php?player=uBored",
            status=200,
            body=html,
        )
        client = mcsrvstats_client

        with pytest.raises(exceptions.exceptions.PlayerNotFoundError):
            await client.universocraft("uBored")


@pytest.mark.asyncio
async def test_universocraft_maintenance(mcsrvstats_client: Client) -> None:
    """Checks universocraft returns correct data when a game is under mantiance."""
    f = open("tests/html/test_universocraft_maintenance.html")
    html = f.read()
    with aioresponses() as m:
        m.get(
            "https://stats.universocraft.com/stats.php?player=uBored",
            status=200,
            body=html,
        )
        client = mcsrvstats_client

        with pytest.raises(exceptions.exceptions.ApiError):
            await client.universocraft("uBored")

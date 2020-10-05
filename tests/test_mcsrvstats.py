"""Main tests."""

import asyncio

import pytest

from mcsrvstats import __version__, Client
from tests.aiohttp import CaseControlledTestServer, http_redirect
from tests.certificate import ssl_certificate, TemporaryCertificate  # noqa: F401

TIMEOUT = 1


def test_version() -> None:
    """Mock version."""
    assert __version__ == "0.2.0"


@pytest.mark.asyncio
async def test_hiveMCAchievements(http_redirect):  # noqa: F401
    async with CaseControlledTestServer() as server:
        http_redirect.add_server("api.hivemc.com", 80, server.port)
        client = Client(session=http_redirect.session)

        task = asyncio.ensure_future(client.hiveMCAchievements("Lord_Ewout"))
        request = await server.receive_request(timeout=TIMEOUT)
        assert request.path_qs == "/v1/player/Lord_Ewout"

        server.send_response(
            request,
            text='{"username":"Lord_Ewout","rankName":"Regular Hive Member","l'
            + 'egacyRank":null,"modernRank":{"enum":"EMERALD","human":"Emerald P'
            + 'remium","index":30},"tokens":6390538,"credits":0,"medals":4282,"c'
            + 'rates":0,"UUID":"a12d8264f19746e6878a0ab9ac8617ac","status":{"des'
            + 'cription":"Currently hibernating in","game":"the Land of Nods!"},'
            + '"cached":1601853120,"firstLogin":1372006132,"lastLogin":159502195'
            + '1,"lastLogout":1595021964,"achievements":{"THESWARM":{"progress":'
            + '1,"unlockedAt":1422286300,"from":"079a7d06aa054ab2be047ce81842755'
            + '6","game":"HideAndSeek"},"SPREDDIT":{"progress":25,"unlockedAt":1'
            + '424440011},"FRIENDJOINFRIEND":{"progress":1,"unlockedAt":14221995'
            + '71},"HUB":{"progress":1,"unlockedAt":1422192681},"DENIED":{"progr'
            + 'ess":1,"unlockedAt":1422193105},"FRIENDACCEPTINVITE":{"progress":'
            + '1,"unlockedAt":1422193671},"FRIEND10":{"progress":1,"unlockedAt":'
            + '1422192567},"FRIENDMSG":{"progress":1,"unlockedAt":1422192697},"F'
            + 'RIENDDENY":{"progress":1,"unlockedAt":1422193650},"FRIEND1":{"pro'
            + 'gress":1,"unlockedAt":1422192567},"FRIENDREMOVE":{"progress":1,"u'
            + 'nlockedAt":1422211225},"PLAY1":{"progress":1,"unlockedAt":1422207'
            + '989},"SESSION3":{"progress":1,"unlockedAt":1422224679},"PLAY24":{'
            + '"progress":1,"unlockedAt":1422544015},"PLAY168":{"progress":1,"un'
            + 'lockedAt":1424275234},"FRIENDINVITE":{"progress":1,"unlockedAt":1'
            + '427914832},"PARTYDISBAND":{"progress":1,"unlockedAt":1468502987},'
            + '"PARTYOWNER":{"progress":1,"unlockedAt":1468501324},"PARTYTELEPOR'
            + 'T":{"progress":1,"unlockedAt":1468501060},"PARTYACCEPT":{"progres'
            + 's":1,"unlockedAt":1468500450},"PARTYINVITE":{"progress":1,"unlock'
            + 'edAt":1468501621},"PARTYLEAVE":{"progress":1,"unlockedAt":1468704'
            + '418},"PARTYKICK":{"progress":1,"unlockedAt":1469725361},"PARTYMAX'
            + '":{"progress":1,"unlockedAt":1474731094},"JOIN3":{"progress":1,"u'
            + 'nlockedAt":1485389316},"JOIN1":{"progress":1,"unlockedAt":1485389'
            + '316},"JOIN2":{"progress":1,"unlockedAt":1485389316},"JOIN4":{"pro'
            + 'gress":1,"unlockedAt":1516649753},"FRIENDFAVORITE":{"progress":1,'
            + '"unlockedAt":1529523010},"JOIN5":{"progress":1,"unlockedAt":15297'
            + '92911},"JOIN6":{"progress":1,"unlockedAt":1567552622}},"trophies"'
            + ':[{"game":"Global","achievement":"JOIN3"},{"game":"Global","achie'
            + 'vement":"JOIN2"},{"game":"Global","achievement":"JOIN5"},{"game":'
            + '"Global","achievement":"JOIN6"},{"game":"BP","achievement":"MASTE'
            + 'R"},{"game":"Global","achievement":"JOIN1"},{"game":"Global","ach'
            + 'ievement":"JOIN4"}]}',
            content_type="application/json",
        )
        result = await asyncio.wait_for(task, TIMEOUT)
        assert result == {
            "all_achievements": [
                "THESWARM",
                "SPREDDIT",
                "FRIENDJOINFRIEND",
                "HUB",
                "DENIED",
                "FRIENDACCEPTINVITE",
                "FRIEND10",
                "FRIENDMSG",
                "FRIENDDENY",
                "FRIEND1",
                "FRIENDREMOVE",
                "PLAY1",
                "SESSION3",
                "PLAY24",
                "PLAY168",
                "FRIENDINVITE",
                "PARTYDISBAND",
                "PARTYOWNER",
                "PARTYTELEPORT",
                "PARTYACCEPT",
                "PARTYINVITE",
                "PARTYLEAVE",
                "PARTYKICK",
                "PARTYMAX",
                "JOIN3",
                "JOIN1",
                "JOIN2",
                "JOIN4",
                "FRIENDFAVORITE",
                "JOIN5",
                "JOIN6",
            ]
        }

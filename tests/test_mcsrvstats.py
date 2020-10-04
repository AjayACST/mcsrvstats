"""Main tests."""

import asyncio
import socket
from collections import namedtuple

import aiohttp
import pytest

from mcsrvstats import __version__, Client
from tests.aiohttp import http_redirect, CaseControlledTestServer
from tests.certificate import ssl_certificate, TemporaryCertificate

TIMEOUT = 1


def test_version() -> None:
    """Mock version."""
    assert __version__ == "0.2.0"


@pytest.mark.asyncio
async def test_hiveMCAchievements(http_redirect):
    async with CaseControlledTestServer() as server:
        http_redirect.add_server("api.hivemc.com", 80, server.port)
        client = Client(session=http_redirect.session)

        task = asyncio.ensure_future(client.hiveMCAchievements("Lord_Ewout"))
        request = await server.receive_request(timeout=TIMEOUT)
        assert request.path_qs == "/v1/player/Lord_Ewout"

        server.send_response(
            request,
            text='{"username":"Lord_Ewout","rankName":"Regular Hive Member","legacyRank":null,"modernRank":{"enum":"EMERALD","human":"Emerald Premium","index":30},"tokens":6390538,"credits":0,"medals":4282,"crates":0,"UUID":"a12d8264f19746e6878a0ab9ac8617ac","status":{"description":"Currently hibernating in","game":"the Land of Nods!"},"cached":1601853120,"firstLogin":1372006132,"lastLogin":1595021951,"lastLogout":1595021964,"achievements":{"THESWARM":{"progress":1,"unlockedAt":1422286300,"from":"079a7d06aa054ab2be047ce818427556","game":"HideAndSeek"},"SPREDDIT":{"progress":25,"unlockedAt":1424440011},"FRIENDJOINFRIEND":{"progress":1,"unlockedAt":1422199571},"HUB":{"progress":1,"unlockedAt":1422192681},"DENIED":{"progress":1,"unlockedAt":1422193105},"FRIENDACCEPTINVITE":{"progress":1,"unlockedAt":1422193671},"FRIEND10":{"progress":1,"unlockedAt":1422192567},"FRIENDMSG":{"progress":1,"unlockedAt":1422192697},"FRIENDDENY":{"progress":1,"unlockedAt":1422193650},"FRIEND1":{"progress":1,"unlockedAt":1422192567},"FRIENDREMOVE":{"progress":1,"unlockedAt":1422211225},"PLAY1":{"progress":1,"unlockedAt":1422207989},"SESSION3":{"progress":1,"unlockedAt":1422224679},"PLAY24":{"progress":1,"unlockedAt":1422544015},"PLAY168":{"progress":1,"unlockedAt":1424275234},"FRIENDINVITE":{"progress":1,"unlockedAt":1427914832},"PARTYDISBAND":{"progress":1,"unlockedAt":1468502987},"PARTYOWNER":{"progress":1,"unlockedAt":1468501324},"PARTYTELEPORT":{"progress":1,"unlockedAt":1468501060},"PARTYACCEPT":{"progress":1,"unlockedAt":1468500450},"PARTYINVITE":{"progress":1,"unlockedAt":1468501621},"PARTYLEAVE":{"progress":1,"unlockedAt":1468704418},"PARTYKICK":{"progress":1,"unlockedAt":1469725361},"PARTYMAX":{"progress":1,"unlockedAt":1474731094},"JOIN3":{"progress":1,"unlockedAt":1485389316},"JOIN1":{"progress":1,"unlockedAt":1485389316},"JOIN2":{"progress":1,"unlockedAt":1485389316},"JOIN4":{"progress":1,"unlockedAt":1516649753},"FRIENDFAVORITE":{"progress":1,"unlockedAt":1529523010},"JOIN5":{"progress":1,"unlockedAt":1529792911},"JOIN6":{"progress":1,"unlockedAt":1567552622}},"trophies":[{"game":"Global","achievement":"JOIN3"},{"game":"Global","achievement":"JOIN2"},{"game":"Global","achievement":"JOIN5"},{"game":"Global","achievement":"JOIN6"},{"game":"BP","achievement":"MASTER"},{"game":"Global","achievement":"JOIN1"},{"game":"Global","achievement":"JOIN4"}]}',
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

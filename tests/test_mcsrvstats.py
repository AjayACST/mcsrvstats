"""Main tests."""
import aiohttp
import pytest
import mcsrvstats
from aioresponses import aioresponses
from mcsrvstats import __version__
from mcsrvstats import Client
from mcsrvstats import exceptions


def test_version() -> None:
    """Mock version."""
    assert __version__ == "1.0.0"


@pytest.mark.asyncio
async def test_client_json(mcsrvstats_client: Client) -> None:
    """Test JSON output from URL."""
    with aioresponses() as m:
        m.get(
            "https://api.wynncraft.com/v2/player/IceWarox/stats",
            status=200,
            payload={
                "kind": "wynncraft/player/IceWarox/stats",
                "code": 200,
                "timestamp": 1619819876728,
                "version": "2.1.0",
            },
        )
        client = mcsrvstats_client
        data = await client._get_json(
            "https://api.wynncraft.com/v2/player/IceWarox/stats"
        )

        assert data["kind"] == "wynncraft/player/IceWarox/stats"
        assert data["code"] == 200
        assert data["timestamp"] == 1619819876728
        assert data["version"] == "2.1.0"


@pytest.mark.asyncio
async def test_client_json_error(mcsrvstats_client: Client) -> None:
    """Test JSON output from URL when there is an error."""
    with aioresponses() as m:
        m.get("https://api.wynncraft.com/v2/player/IceWarox/stats", status=500)
        client = mcsrvstats_client
        with pytest.raises(exceptions.exceptions.ApiError):
            await client._get_json("https://api.wynncraft.com/v2/player/IceWarox/stats")


@pytest.mark.asyncio
async def test_client_aiotthp() -> None:
    """Test mcsrvstats client with aiohttp passed to it."""
    aiosession = aiohttp.ClientSession()
    client = mcsrvstats.Client(session=aiosession)
    assert client.session == aiosession

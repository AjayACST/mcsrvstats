"""Pytest fixtures."""
from typing import AsyncIterator

import pytest
from mcsrvstats import Client


@pytest.fixture
async def mcsrvstats_client() -> AsyncIterator[Client]:
    """Mcsrvstats client fixture."""
    client = Client()
    yield client
    await client.close()

"""Pytest fixtures."""
from mcsrvstats import Client
from typing import AsyncIterator

import pytest


@pytest.fixture
async def mcsrvstats_client() -> AsyncIterator[Client]:
    """Mcsrvstats client fixture."""
    client = Client()
    yield client
    await client.close()

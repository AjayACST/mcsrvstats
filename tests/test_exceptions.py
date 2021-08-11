"""Test for mcsrvstats exceptions."""
import pytest
from mcsrvstats import exceptions


@pytest.mark.asyncio
async def test_api_error() -> None:
    """Check ApiError correctly gets raised."""
    with pytest.raises(exceptions.exceptions.ApiError) as e:
        raise exceptions.exceptions.ApiError("An error occurred.")
    assert str(e.value) == "The unknown sourceAPI had An error occurred."


@pytest.mark.asyncio
async def test_player_not_found_error() -> None:
    """Check PlayerNotFoundError correctly gets raised."""
    with pytest.raises(exceptions.exceptions.PlayerNotFoundError) as e:
        raise exceptions.exceptions.PlayerNotFoundError("Player not found.")
    assert str(e.value) == "The player Player not found. could not be found."

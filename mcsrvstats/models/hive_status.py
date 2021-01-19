"""Hive Status related objects."""
from pydantic import BaseModel


class HiveStatus(BaseModel):
    """Hive Status Model.

    Args:
        description (str): Description of the game the player is playing.
        game (str): The game the player is playing.
    """

    description: str
    game: str

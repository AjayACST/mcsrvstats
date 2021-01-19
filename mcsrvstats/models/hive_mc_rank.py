"""Hive rank related objects."""
from pydantic import BaseModel


class HiveRank(BaseModel):
    """Hive rank model.

    Args:
        rank (str): The current players rank.
    """

    rank: str

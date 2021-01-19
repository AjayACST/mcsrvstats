"""Hive Achievements related objects."""
from typing import List

from pydantic import BaseModel


class HiveAchievements(BaseModel):
    """Hive Achievements Model.

    Args:
        all_achievements (List[str]): A list of all achievements on the hive network.
    """

    all_achievements: List[str]

"""Wyncraft Classes related objects."""
from typing import List

from pydantic import BaseModel


class Classes(BaseModel):
    """Model for wyncraft classes.

    Args:
        class_name (str): The name of the players class.
        class_level (int): The level of the players class.
        class_deaths (int): How many deaths the player has in this class.
    """

    class_name: str
    class_level: int
    class_deaths: int


class WyncraftClasses(BaseModel):
    """Wyncraft Classes model.

    Args:
        classes (List[str]): List of the players classes on wyncraft.
    """

    classes: List[Classes]

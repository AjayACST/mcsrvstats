"""Wyncraft Classes related objects."""
from typing import List

from pydantic import BaseModel
from pydantic import Field


class Classes(BaseModel):
    """Model for wyncraft classes.

    Args:
        class_name (str): The name of the players class.
        class_level (int): The level of the players class.
        class_deaths (int): How many deaths the player has in this class.
        class_chest (int): How many chests the player has found.
        class_logins (int): How many logins the player has in this class.
        class_events_won (int): How many events the player has won in this class.
        class_discoveries (int): How many discoveries the player has made in this class.
    """

    class_name: str = Field(alias="name")
    class_level: int = Field(alias="level")
    class_deaths: int = Field(alias="deaths")
    class_chest: int = Field(alias="chestsFound")
    class_logins: int = Field(alias="logins")
    class_events_won: int = Field(alias="eventsWon")
    class_discoveries: int = Field(alias="discoveries")


class WyncraftClasses(BaseModel):
    """Wyncraft Classes model.

    Args:
        classes (List[str]): List of the players classes on wyncraft.
    """

    classes: List[Classes]

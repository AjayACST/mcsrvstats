"""Veltpvp related objects."""
from pydantic import BaseModel
from pydantic import Field


class HCF(BaseModel):
    """Model for HCF stats for veltpvp.

    Args:
        Kills (int): The number of kills the player has.
        Deaths (int): The number of deaths the player has.
        KDR (float): The KDR of the player.
        Lives (int): The number of lives the player has.
        Playtime (int): The amount of playtime the player has.
    """

    Kills: int = Field(alias="Kills")
    Deaths: int = Field(alias="Deaths")
    KDR: float = Field(alias="KDR")
    Lives: int = Field(alias="Lives")
    Playtime: str = Field(alias="Playtime")


class Practice(BaseModel):
    """Model for Practice stats for veltpvp.

    Args:
        Kills (int): The number of kills the player has.
        Deaths (int): The number of deaths the player has.
        Wins (int): The number of wins the player has.
        Losses (int): The number of losses the player has.
        Fights (int): The number of fights the player has had.
        GlobalELO (int): The players total Global ELO.
    """

    Kills: int
    Deaths: int
    Wins: int
    Losses: int
    Fights: int
    GlobalELO: int = Field(alias="Global ELO")


class Soup(BaseModel):
    """Model for Soup stats for veltpvp.

    Args:
        Kills (int): The number of kills the player has.
        Deaths (int): The number of deaths the player has.
        HighestKillstreak (int): The highest killstreak the player has.
        EventsWon (int): The number of events the player has won.
        EventsLost (int): The number of events the player has lost.
    """

    Kills: int
    Deaths: int
    HighestKillstreak: int = Field(alias="Highest Killstreak")
    EventsWon: int = Field(alias="Events Won")
    EventsLost: int = Field(alias="Events Lost")


class Veltpvp(BaseModel):
    """VeltPVP stats model.

    Args:
        Rank (str): The rank the player has.
        LastSeen (str): How long ago the player was last seen.
        CurrentStatus (str): The player's current status.
        FirstJoined (str): When the player first joined the server.
        TimePlayed (str): Total amount of time played on the server.
        MonthlyViews (int): The number of monthly views the player has.
        HCF (HCF): HCF stats for the player.
        Practice (Practice): Practice stats for the player.
        Soup (Soup): Soup stats for the player.
    """

    Rank: str
    LastSeen: str
    CurrentStatus: str
    FirstJoined: str
    TimePlayed: str
    MonthlyViews: int
    HCF: HCF
    Practice: Practice
    Soup: Soup

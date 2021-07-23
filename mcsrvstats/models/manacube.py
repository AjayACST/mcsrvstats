"""Manacube related objects."""
from typing import Optional, Any

from datetime import datetime

from pydantic import BaseModel, validator


class Parkour(BaseModel):
    """Parkour model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mana (int): How much mana the player has.
        score (int): The players score.
        courses (int): How many courses the player has done.
    """

    playtime: str = "No Time"
    mana: Optional[int] = 0
    score: Optional[int] = 0
    courses: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Aztec(BaseModel):
    """Aztec model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (int): How many mobs the player has killed.
        mana (int): How much mana the player has.
        money (int): How much money the player has.
    """

    playtime: str = "No Time"
    mobkills: Optional[int] = 0
    mana: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Oasis(BaseModel):
    """Oasis model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobkills (int): How many mobs the player has killed.
        mana (int): How much mana the player has.
        money (int): How many quests the player has completed.
    """

    playtime: str = "No Time"
    mobkills: Optional[int] = 0
    mana: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Islands(BaseModel):
    """Islands model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (int): How many mobs the player has killed.
        silver (int): How much silver the player has.
        money (int): How much money the player has.
    """

    playtime: str = "No Time"
    mobkills: Optional[int] = 0
    silver: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Survival(BaseModel):
    """Survival model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (int): How many mobs the player has killed.
        money (int): How much money the player has.
        quests (int): How many quests the player has completed.
    """

    playtime: str = "No Time"
    mobkills: Optional[int] = 0
    money: Optional[int] = 0
    quests: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Factions(BaseModel):
    """Factions model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        kills (int): How many kills the player has.
        mobkills (int): How many mobs the player has killed.
        money (int): How much money the player has.
    """

    playtime: str = "No Time"
    kills: Optional[int] = 0
    mobkills: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Aether(BaseModel):
    """Aether model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (int): The players mining level.
        money (int): How much money the player has.
        rebirths (int): How many rebirths the player has had.
    """

    playtime: str = "No Time"
    mininglevel: Optional[int] = 0
    money: Optional[int] = 0
    rebirths: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Atlas(BaseModel):
    """Atlas model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (int): The players mining level.
        money (int): How much money the player has.
        rebirths (int): How many rebirths the player has had.
    """

    playtime: str = "No Time"
    mininglevel: Optional[int] = 0
    money: Optional[int] = 0
    rebirths: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Creative(BaseModel):
    """Creative model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        blocksplaced (int): How many blocks the player has placed.
        blocksbroken (int): How many blocks the player has broken.
    """

    playtime: str = "No Time"
    blocksplaced: Optional[int] = 0
    blocksbroken: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Kitpvp(BaseModel):
    """Kitpvp model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        level (int): The players level.
        money (int): How much money the player has.
        kills (int): How many kills the player has.
    """

    playtime: str = "No Time"
    level: Optional[int] = 0
    money: Optional[int] = 0
    kills: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls: Any, v: Any, field: Any) -> Any:
        if v == "N/A":
            return field.default
        return v


class Manacube(BaseModel):
    """Manacube model.

    Args:
        exists (bool): If the player exists
        level (int): The players level.
        rank (str): The players rank.
        cubits (float): The players amount of cubits.
        firstSeen (datetime): When the player first joined.
        lastSeen (datetime): When the player was last on the server.
        lastSeenAgo (str): Amount of time since the player was last seen.
        Parkour (Parkour): Parkour stats.
        Aztec (Aztec): Aztec stats.
        Oasis (Oasis): Oasis stats.
        Islands (Islands): Islands stats.
        Survival (Survival): Survival stats.
        Factions (Factions): Factions stats.
        Aether (Aether): Aether stats.
        Atlas (Atlas): Atlas stats.
        Creative (Creative): Creative stats.
        Kitpvp (Kitpvp): Kitpvp stats.
    """

    exists: bool
    level: int
    rank: str
    cubits: float
    firstseen: datetime
    lastseen: datetime
    lastseenago: str
    parkour: Parkour
    aztec: Aztec
    oasis: Oasis
    islands: Islands
    survival: Survival
    factions: Factions
    aether: Aether
    atlas: Atlas
    creative: Creative
    kitpvp: Kitpvp

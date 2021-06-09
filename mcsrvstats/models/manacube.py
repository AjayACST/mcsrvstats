"""Manacube related objects."""
from typing import Optional

from datetime import datetime

from pydantic import BaseModel, validator


class Parkour(BaseModel):
    """Parkour model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mana (str): How much mana the player has.
        score (str): The players score.
        courses (str): How many courses the player has done.
    """

    playtime: Optional[str] = "No Time"
    mana: Optional[int] = 0
    score: Optional[int] = 0
    courses: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Aztec(BaseModel):
    """Aztec model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "No Time"
    mobkills: Optional[int] = 0
    mana: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Oasis(BaseModel):
    """Oasis model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobkills (str): How many mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How many quests the player has completed.
    """

    playtime: Optional[str] = "No Time"
    mobkills: Optional[int] = 0
    mana: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Islands(BaseModel):
    """Islands model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        silver (str): How much silver the player has.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "No Time"
    mobkills: Optional[int] = 0
    silver: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Survival(BaseModel):
    """Survival model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        money (str): How much money the player has.
        quests (str): How many quests the player has completed.
    """

    playtime: Optional[str] = "No Time"
    mobkills: Optional[int] = 0
    money: Optional[int] = 0
    quests: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Factions(BaseModel):
    """Factions model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        kills (str): How many kills the player has.
        mobkills (str): How many mobs the player has killed.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "No Time"
    kills: Optional[int] = 0
    mobkills: Optional[int] = 0
    money: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Aether(BaseModel):
    """Aether model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: Optional[str] = "No Time"
    mininglevel: Optional[int] = 0
    money: Optional[int] = 0
    rebirths: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Atlas(BaseModel):
    """Atlas model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: Optional[str] = "No Time"
    mininglevel: Optional[int] = 0
    money: Optional[int] = 0
    rebirths: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Creative(BaseModel):
    """Creative model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        blocksplaced (str): How many blocks the player has placed.
        blocksbroken (str): How many blocks the player has broken.
    """

    playtime: Optional[str] = "No Time"
    blocksplaced: Optional[int] = 0
    blocksbroken: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Kitpvp(BaseModel):
    """Kitpvp model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        level (str): The players level.
        money (str): How much money the player has.
        kills (str): How many kills the player has.
    """

    playtime: Optional[str] = "No Time"
    level: Optional[int] = 0
    money: Optional[int] = 0
    kills: Optional[int] = 0

    @validator('*', pre=True)
    def name_must_contain_space(cls, v, field):
        if v == "N/A":
            return field.default
        return v


class Manacube(BaseModel):
    """Manacube model.

    Args:
        exists (str): If the player exists
        level (str): The players level.
        rank (str): The players rank.
        cubits (str): The players amount of cubits.
        firstSeen (str): When the player first joined.
        lastSeen (str): When the player was last on the server.
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

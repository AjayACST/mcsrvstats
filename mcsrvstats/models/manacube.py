"""Manacube related objects."""
from typing import Optional

from pydantic import BaseModel


class Parkour(BaseModel):
    """Parkour model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mana (str): How much mana the player has.
        score (str): The players score.
        courses (str): How many courses the player has done.
    """

    playtime: Optional[str] = "N/A"
    mana: Optional[str] = "N/A"
    score: Optional[str] = "N/A"
    courses: Optional[str] = "N/A"


class Aztec(BaseModel):
    """Aztec model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How ma-ny mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "N/A"
    mobkills: Optional[str] = "N/A"
    mana: Optional[str] = "N/A"
    money: Optional[str] = "N/A"


class Oasis(BaseModel):
    """Oasis model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobkills (str): How many mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How many quests the player has completed.
    """

    playtime: Optional[str] = "N/A"
    mobkills: Optional[str] = "N/A"
    mana: Optional[str] = "N/A"
    money: Optional[str] = "N/A"


class Islands(BaseModel):
    """Islands model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        silver (str): How much silver the player has.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "N/A"
    mobkills: Optional[str] = "N/A"
    silver: Optional[str] = "N/A"
    money: Optional[str] = "N/A"


class Survival(BaseModel):
    """Survival model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        money (str): How much money the player has.
        quests (str): How many quests the player has completed.
    """

    playtime: Optional[str] = "N/A"
    mobkills: Optional[str] = "N/A"
    money: Optional[str] = "N/A"
    quests: Optional[str] = "N/A"


class Factions(BaseModel):
    """Factions model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        kills (str): How many kills the player has.
        mobkills (str): How many mobs the player has killed.
        money (str): How much money the player has.
    """

    playtime: Optional[str] = "N/A"
    kills: Optional[str] = "N/A"
    mobkills: Optional[str] = "N/A"
    money: Optional[str] = "N/A"


class Aether(BaseModel):
    """Aether model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: Optional[str] = "N/A"
    mininglevel: Optional[str] = "N/A"
    money: Optional[str] = "N/A"
    rebirths: Optional[str] = "N/A"


class Atlas(BaseModel):
    """Atlas model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: Optional[str] = "N/A"
    mininglevel: Optional[str] = "N/A"
    money: Optional[str] = "N/A"
    rebirths: Optional[str] = "N/A"


class Creative(BaseModel):
    """Creative model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        blocksplaced (str): How many blocks the player has placed.
        blocksbroken (str): How many blocks the player has broken.
    """

    playtime: Optional[str] = "N/A"
    blocksplaced: Optional[str] = "N/A"
    blocksbroken: Optional[str] = "N/A"


class Kitpvp(BaseModel):
    """Kitpvp model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        level (str): The players level.
        money (str): How much money the player has.
        kills (str): How many kills the player has.
    """

    playtime: Optional[str] = "N/A"
    level: Optional[str] = "N/A"
    money: Optional[str] = "N/A"
    kills: Optional[str] = "N/A"


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

    exists: Optional[str] = "N/A"
    level: Optional[str] = "N/A"
    rank: Optional[str] = "N/A"
    cubits: Optional[str] = "N/A"
    firstseen: Optional[str] = "N/A"
    lastseen: Optional[str] = "N/A"
    lastseenago: Optional[str] = "N/A"
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

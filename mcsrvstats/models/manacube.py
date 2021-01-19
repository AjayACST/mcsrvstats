"""Manacube related objects."""
from pydantic import BaseModel


class Parkour(BaseModel):
    """Parkour model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mana (str): How much mana the player has.
        score (str): The players score.
        courses (str): How many courses the player has done.
    """

    playtime: str
    mana: str
    score: str
    courses: str


class Aztec(BaseModel):
    """Aztec model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How ma-ny mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How much money the player has.
    """

    playtime: str
    mobkills: str
    mana: str
    money: str


class Oasis(BaseModel):
    """Oasis model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobkills (str): How many mobs the player has killed.
        mana (str): How much mana the player has.
        money (str): How many quests the player has completed.
    """

    playtime: str
    mobkills: str
    mana: str
    money: str


class Islands(BaseModel):
    """Islands model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        silver (str): How much silver the player has.
        money (str): How much money the player has.
    """

    playtime: str
    mobkills: str
    silver: str
    money: str


class Survival(BaseModel):
    """Survival model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        mobKills (str): How many mobs the player has killed.
        money (str): How much money the player has.
        quests (str): How many quests the player has completed.
    """

    playtime: str
    mobkills: str
    money: str
    quests: str


class Factions(BaseModel):
    """Factions model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        kills (str): How many kills the player has.
        mobkills (str): How many mobs the player has killed.
        money (str): How much money the player has.
    """

    playtime: str
    kills: str
    mobkills: str
    money: str


class Aether(BaseModel):
    """Aether model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: str
    mininglevel: str
    money: str
    rebirths: str


class Atlas(BaseModel):
    """Atlas model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        miningLevel (str): The players mining level.
        money (str): How much money the player has.
        rebirths (str): How many rebirths the player has had.
    """

    playtime: str
    mininglevel: str
    money: str
    rebirths: str


class Creative(BaseModel):
    """Creative model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        blocksplaced (str): How many blocks the player has placed.
        blocksbroken (str): How many blocks the player has broken.
    """

    playtime: str
    blocksplaced: str
    blocksbroken: str


class Kitpvp(BaseModel):
    """Kitpvp model for manacube.

    Args:
        playtime (str): How many hours the player has played for.
        level (str): The players level.
        money (str): How much money the player has.
        kills (str): How many kills the player has.
    """

    playtime: str
    level: str
    money: str
    kills: str


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

    exists: str
    level: str
    rank: str
    cubits: str
    firstseen: str
    lastseen: str
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

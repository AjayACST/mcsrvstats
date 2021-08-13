"""Gomehd related objects."""
from pydantic import BaseModel
from pydantic import Field


class TTT(BaseModel):
    """TTT model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        karma (int): How much karma the player has.
        deaths (int): How many deaths the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    karma: int = Field(alias="Karma")
    deaths: int = Field(alias="Deaths")


class BedWarsGomme(BaseModel):
    """BedWars model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        games (int): How many games the player has played.
        BedsDestroyed (int): How many beds the player has destroyed.
        deaths (int): How many deaths the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    games: int = Field(alias="Games")
    BedsDestroyed: int = Field(alias="Beds destroyed")
    deaths: int = Field(alias="Deaths")


class SkyWarsGomme(BaseModel):
    """SkyWars model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")


class SurvivalGames(BaseModel):
    """Survival Games model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
        points (int): How many points the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")
    points: int = Field(alias="Points")


class EnderGames(BaseModel):
    """EnderGames model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")


class QuickSurvivalGames(BaseModel):
    """Survival Games model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
        points (int): How many points the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")
    points: int = Field(alias="Points")


class Cores(BaseModel):
    """Cores model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")


class GunGame(BaseModel):
    """Cores model for gommehd.

    Args:
        kills (int): How many kills the player has.
    """

    kills: int = Field(alias="Kills")


class SpeedUHC(BaseModel):
    """SpeedUHC Games model for gommehd.

    Args:
        wins (int): How many wins the player has.
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
        points (int): How many points the player has.
    """

    wins: int = Field(alias="Wins")
    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")
    points: int = Field(alias="Points")


class MasterBuilders(BaseModel):
    """MasterBuilders Games model for gommehd.

    Args:
        wins (int): How many wins the player has.
        games (int): How many games the player has played.
        points (int): How many points the player has.
    """

    wins: int = Field(alias="Wins")
    games: int = Field(alias="Games")
    points: int = Field(alias="Points")


class Cookies(BaseModel):
    """Cookies Games model for gommehd.

    Args:
        wins (int): How many wins the player has.
        cookies (int): How many cookies the player has.
    """

    wins: int = Field(alias="Wins")
    cookies: int = Field(alias="Cookies")


class Hardcore(BaseModel):
    """Hardcore Games model for gommehd.

    Args:
        kills (int): How many kills the player has.
        deaths (int): How many deaths the player has.
    """

    kills: int = Field(alias="Kills")
    deaths: int = Field(alias="Deaths")


class GommeHD(BaseModel):
    """Gommehd model.

    Args:
        TTT (TTT): TTT Stats.
        BedWars (BedWars): BedWars stats.
        SkyWars (SkyWars): SkyWars stats.
        SurvivalGames (SurvivalGames): SurvivalGames stats.
        EnderGames (EnderGames): EnderGames stats.
        QuickSurvivalGames (QuickSurvivalGames): QuickSurvivalGames stats.
        Cores (Cores): Cores stats.
        GunGame (GunGame): GunGame stats.
        SpeedUHC (SpeedUHC): SpeedUHC stats.
        MasterBuilders (MasterBuilders): MasterBuilders stats.
        Cookies (Cookies): Cookies stats.
        Hardcore (Hardcore): Hardcore stats.
    """

    TTT: TTT
    BedWars: BedWarsGomme
    SkyWars: SkyWarsGomme
    SurvivalGames: SurvivalGames
    EnderGames: EnderGames
    QuickSurvivalGames: QuickSurvivalGames
    Cores: Cores
    GunGame: GunGame
    SpeedUHC: SpeedUHC
    MasterBuilders: MasterBuilders
    Cookies: Cookies
    Hardcore: Hardcore

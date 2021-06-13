"""Gomehd related objects."""
from pydantic import BaseModel, Field

class TTT(BaseModel):
    """TTT model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Karma (int): How much karma the player has.
        Deaths (int): How many deaths the player has.
    """

    Wins: int
    Kills: int
    Karma: int
    Deaths: int

class BedWarsGomme(BaseModel):
    """BedWars model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Games (int): How many games the player has played.
        BedsDestroyed (int): How many beds the player has destroyed.
        Deaths (int): How many deaths the player has.
    """

    Wins: int
    Kills: int
    Games: int
    BedsDestroyed: int = Field(alias="Beds destroyed")
    Deaths: int

class SkyWarsGomme(BaseModel):
    """SkyWars model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
    """

    Wins: int
    Kills: int
    Deaths: int

class SurvivalGames(BaseModel):
    """Survival Games model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
        Points (int): How many points the player has.
    """

    Wins: int
    Kills: int
    Deaths: int
    Points: int

class EnderGames(BaseModel):
    """EnderGames model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
    """

    Wins: int
    Kills: int
    Deaths: int

class QuickSurvivalGames(BaseModel):
    """Survival Games model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
        Points (int): How many points the player has.
    """

    Wins: int
    Kills: int
    Deaths: int
    Points: int

class Cores(BaseModel):
    """Cores model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
    """

    Wins: int
    Kills: int
    Deaths: int

class GunGame(BaseModel):
    """Cores model for gommehd.

    Args:
        Kills (int): How many kills the player has.
    """

    Kills: int

class SpeedUHC(BaseModel):
    """SpeedUHC Games model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
        Points (int): How many points the player has.
    """

    Wins: int
    Kills: int
    Deaths: int
    Points: int

class MasterBuilders(BaseModel):
    """MasterBuilders Games model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Games (int): How many games the player has played.
        Points (int): How many points the player has.
    """

    Wins: int
    Games: int
    Points: int

class Cookies(BaseModel):
    """Cookies Games model for gommehd.

    Args:
        Wins (int): How many wins the player has.
        Cookies (int): How many cookies the player has.
    """

    Wins: int
    Cookies: int

class Hardcore(BaseModel):
    """Hardcore Games model for gommehd.

    Args:
        Kills (int): How many kills the player has.
        Deaths (int): How many deaths the player has.
    """

    Kills: int
    Deaths: int

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
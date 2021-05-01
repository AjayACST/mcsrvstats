"""Universocraft related objects."""
from pydantic import BaseModel


class DestoryNexus(BaseModel):
    """Model for Destory Nexus.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        archedmurders (int): Number of arched murders.
        deaths (int): Number of deaths.
        damagenexus (int): Amount of damage delt to the nexus.
        nexusdestructions (int): Amount of Nexus Destructions
        blocksplaced (int): Amount of blocks placed.
        destroyedblocks (int): Amount of blocks destroyed.
        minesdestroyed (int): Amount of mines destroyed.
        trunksdestroyed (int): Amount of trunks destroyed.
    """

    victories: int
    murders: int
    archedmurders: int
    deaths: int
    damagenexus: int
    nexusdestructions: int
    blocksplaced: int
    destroyedblocks: int
    minesdestroyed: int
    trunksdestroyed: int


class SkyWars(BaseModel):
    """Model for SkyWars and LuckyWars and TeamSkyWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        blocksplaced (int): Number of blocks placed.
        destroyednlockes (int): Number of destroyed blocks.
        projectileslaunch (int): Number of projectiles launched.
        impactedprojectiles (int): Number of impactedProjectiles.
    """

    victories: int
    murders: int
    deaths: int
    blocksplaced: int
    destroyedblocks: int
    projectileslaunch: int
    impactedprojectiles: int


class EggWars(BaseModel):
    """Model for EggWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        brokeneggs (int): Number of broken eggs.
        deaths (int): Number of deaths.
        blocksplaced (int): Number of blocks placed.
        destroyednlockes (int): Number of destroyed blocks.
        projectileslaunch (int): Number of projectiles launched.
        impactedprojectiles (int): Number of impactedProjectiles.
    """

    victories: int
    murders: int
    brokeneggs: int
    deaths: int
    blocksplaced: int
    destroyedblocks: int
    projectileslaunch: int
    impactedprojectiles: int


class BedWars(BaseModel):
    """Model for BedWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        finalmurders (int): Number of final murders.
        destroyedbeds (int): Number of destroyed beds.
        deaths (int): Number of deaths.
        finaldeaths (int): Number of final deaths.
        gamesplayed (int): Number of games played.
    """

    victories: int
    murders: int
    finalmurders: int
    destroyedbeds: int
    deaths: int
    finaldeaths: int
    gamesplayed: int


class SpeedBuilders(BaseModel):
    """Model for SpeedBuilders.

    Args:
        victories (int): Number of victories.
        lost (int): Number of games lost.
        perfectconstructions (int): Number of perfect constructions.
    """

    victories: int
    lost: int
    perfectconstructions: int


class BuildBattle(BaseModel):
    """Model for BuildBattle.

    Args:
        victories (int): Number of victories.
        gamesplayed (int): Number of games played.
        score (int): The player's score.
    """

    victories: int
    gamesplayed: int
    score: int


class EscapeBeast(BaseModel):
    """Model for Escape the Beast.

    Args:
        totalvictories (int): Total number of victories.
        victoriesrunner (int): Number of victories as the runner.
        victoriesbeast (int): Number of victories as the beast.
        murdersrunner (int): Number of murders as the runner
        murdersbeast (int): Number of murders as the beast.
    """

    totalvictories: int
    victoriesrunner: int
    victoriesbeast: int
    murdersrunner: int
    murdersbeast: int


class PartyGames(BaseModel):
    """Model for Party Games.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        gamesplayed (int): Number of games played.
    """

    victories: int
    murders: int
    deaths: int
    gamesplayed: int


class SkyPit(BaseModel):
    """Model for Sky Pit.

    Args:
        level (int): Players level on sky pit.
        unicoins (int): Total number of unicoins.
        assists (int): Total number of assists.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    level: int
    unicoins: int
    assists: int
    murders: int
    deaths: int


class UHC(BaseModel):
    """Model for UHC.

    Args:
        victories (int): Number of victories.
        lost (int): Total number of games lost.
        gamesplayed (int): Total number of games played.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    victories: int
    lost: int
    gamesplayed: int
    murders: int
    deaths: int


class MurderMystery(BaseModel):
    """Model for Murder Mystery.

    Args:
        victories (int): Total number of victories.
        lost (int): Total number of lost games.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    victories: int
    lost: int
    murders: int
    deaths: int


class CaptureWool(BaseModel):
    """Model for Capture the Wool.

    Args:
        socre (int):  The players total score.
        murders (int): Total amount of murders.
        archedmurders (int): Total amount of arched murders.
        maxarchdistance (int): The maximum distance of death with bow.
        woolplaced (int): Total number of blocks of wool placed.
    """

    score: int
    murders: int
    archedmurders: int
    maxarchdistance: int
    woolplaced: int


class Universocraft(BaseModel):
    """Universocraft model.

    Args:
        DestoryNexus (DestoryNexus): DestoryNexus stats.
        SkyWars (SkyWars): SkyWars stats.
        EggWars (EggWars): EggWars stats.
        BedWars (BedWars): BedWars stats.
        SpeedBuilders (SpeedBuilders): SpeedBuilders stats.
        BuildBattle (BuildBattle): BuildBattle stats.
        EscapeBeast (EscapeBeast): Escape the Beast stats.
        PartyGames (PartyGames): PartyGames stats.
        SkyPit (SkyPit): SkyPit stats.
        UHC (UHC): UHC stats.
        MurderMystery (MurderMystery): MurderMystery stats.
        CaptureWool (CaptureWool): Capture the Woll stats.
    """

    DestoryNexus: DestoryNexus
    SkyWars: SkyWars
    EggWars: EggWars
    BedWars: BedWars
    SpeedBuilders: SpeedBuilders
    BuildBattle: BuildBattle
    EscapeBeast: EscapeBeast
    PartyGames: PartyGames
    SkyPit: SkyPit
    UHC: UHC
    MurderMystery: MurderMystery
    CaptureWool: CaptureWool

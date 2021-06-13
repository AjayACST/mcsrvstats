"""Universocraft related objects."""
from pydantic import BaseModel, Field


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
        oresdestroyed (int): Amount of ores destroyed.
        logsdestroyed (int): Amount of logs destroyed.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    archedmurders: int = Field(alias="ASESINATOS CON ARCO")
    deaths: int = Field(alias="MUERTES")
    damagenexus: int = Field(alias="DAÑOS AL NEXUS")
    nexusdestructions: int = Field(alias="DESTRUCCIONES DEL NEXUS")
    blocksplaced: int = Field(alias="BLOQUES COLOCADOS")
    destroyedblocks: int = Field(alias="BLOQUES DESTRUIDOS")
    oresdestroyed: int = Field(alias="MENAS DESTRUIDAS")
    logsdestroyed: int = Field(alias="TRONCOS DESTRUIDOS")


class SkyWars(BaseModel):
    """Model for SkyWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        blocksplaced (int): Number of blocks placed.
        destroyednlockes (int): Number of destroyed blocks.
        projectileslaunch (int): Number of projectiles launched.
        impactedprojectiles (int): Number of impactedProjectiles.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")
    blocksplaced: int = Field(alias="BLOQUES COLOCADOS")
    destroyedblocks: int = Field(alias="BLOQUES DESTRUIDOS")
    projectileslaunch: int = Field(alias="PROJECTILES LANZADOS")
    impactedprojectiles: int = Field(alias="PROJECTILES IMPACTADOS")

class LuckyWars(BaseModel):
    """Model for LuckyWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        blocksplaced (int): Number of blocks placed.
        destroyednlockes (int): Number of destroyed blocks.
        projectileslaunch (int): Number of projectiles launched.
        impactedprojectiles (int): Number of impactedProjectiles.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")
    blocksplaced: int = Field(alias="BLOQUES COLOCADOS")
    destroyedblocks: int = Field(alias="BLOQUES DESTRUIDOS")
    projectileslaunch: int = Field(alias="PROJECTILES LANZADOS")
    impactedprojectiles: int = Field(alias="PROJECTILES IMPACTADOS")

class TeamSkyWars(BaseModel):
    """Model for TeamSkyWars.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        blocksplaced (int): Number of blocks placed.
        destroyednlockes (int): Number of destroyed blocks.
        projectileslaunch (int): Number of projectiles launched.
        impactedprojectiles (int): Number of impactedProjectiles.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")
    blocksplaced: int = Field(alias="BLOQUES COLOCADOS")
    destroyedblocks: int = Field(alias="BLOQUES DESTRUIDOS")
    projectileslaunch: int = Field(alias="PROJECTILES LANZADOS")
    impactedprojectiles: int = Field(alias="PROJECTILES IMPACTADOS")


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

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    brokeneggs: int = Field(alias="HUEVOS ROTOS")
    deaths: int = Field(alias="MUERTES")
    blocksplaced: int = Field(alias="BLOQUES COLOCADOS")
    destroyedblocks: int = Field(alias="BLOQUES DESTRUIDOS")
    projectileslaunch: int = Field(alias="PROJECTILES LANZADOS")
    impactedprojectiles: int = Field(alias="PROJECTILES IMPACTADOS")


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

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    finalmurders: int = Field(alias="ASESINATOS FINALES")
    destroyedbeds: int = Field(alias="CAMAS DESTRUIDAS")
    deaths: int = Field(alias="MUERTES")
    finaldeaths: int = Field(alias="MUERTES FINALES")
    gamesplayed: int = Field(alias="PARTIDAS JUGADAS")


class SpeedBuilders(BaseModel):
    """Model for SpeedBuilders.

    Args:
        victories (int): Number of victories.
        lost (int): Number of games lost.
        perfectconstructions (int): Number of perfect constructions.
    """

    victories: int = Field(alias="VICTORIAS")
    lost: int = Field(alias="PERDIDAS")
    perfectconstructions: int = Field(alias="CONSTRUCCIONES PERFECTAS")


class BuildBattle(BaseModel):
    """Model for BuildBattle.

    Args:
        victories (int): Number of victories.
        gamesplayed (int): Number of games played.
        score (int): The player's score.
    """

    victories: int = Field(alias="VICTORIAS")
    gamesplayed: int = Field(alias="PARTIDAS JUGADAS")
    score: int = Field(alias="PUNTAJE")


class EscapeBeast(BaseModel):
    """Model for Escape the Beast.

    Args:
        totalvictories (int): Total number of victories.
        victoriesrunner (int): Number of victories as the runner.
        victoriesbeast (int): Number of victories as the beast.
        murdersrunner (int): Number of murders as the runner
        murdersbeast (int): Number of murders as the beast.
    """

    totalvictories: int = Field(alias="VICTORIAS TOTALES")
    victoriesrunner: int = Field(alias="VICTORIAS COMO CORREDOR")
    victoriesbeast: int = Field(alias="VICTORIAS COMO BESTIA")
    murdersrunner: int = Field(alias="ASESINATO COMO CORREDOR")
    murdersbeast: int = Field(alias="ASESINATO COMO BESTIA")


class PartyGames(BaseModel):
    """Model for Party Games.

    Args:
        victories (int): Number of victories.
        murders (int): Number of murders.
        deaths (int): Number of deaths.
        gamesplayed (int): Number of games played.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")
    gamesplayed: int = Field(alias="PARTIDAS JUGADAS")


class SkyPit(BaseModel):
    """Model for Sky Pit.

    Args:
        level (int): Players level on sky pit.
        unicoins (int): Total number of unicoins.
        assists (int): Total number of assists.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    level: int = Field(alias="Nivel")
    unicoins: int = Field(alias="UNICOINS")
    assists: int = Field(alias="ASISTENCIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")


class UHC(BaseModel):
    """Model for UHC.

    Args:
        victories (int): Number of victories.
        lost (int): Total number of games lost.
        gamesplayed (int): Total number of games played.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    victories: int = Field(alias="VICTORIAS")
    lost: int = Field(alias="PERDIDAS")
    gamesplayed: int = Field(alias="PARTIDAS JUGADAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")


class MurderMystery(BaseModel):
    """Model for Murder Mystery.

    Args:
        victories (int): Total number of victories.
        lost (int): Total number of lost games.
        murders (int): Total number of murders.
        deaths (int): Total number of deaths.
    """

    victories: int = Field(alias="VICTORIAS")
    lost: int = Field(alias="PERDIDAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")


class CaptureWool(BaseModel):
    """Model for Capture the Wool.

    Args:
        socre (int):  The players total score.
        murders (int): Total amount of murders.
        archedmurders (int): Total amount of arched murders.
        maxarchdistance (int): The maximum distance of death with bow.
        woolplaced (int): Total number of blocks of wool placed.
    """

    score: int = Field(alias="PUNTAJE")
    murders: int = Field(alias="ASESINATOS")
    archedmurders: int = Field(alias="ASESINATOS CON ARCO")
    maxarchdistance: int = Field(alias="DISTANCIA MÁXIMA DE MUERTE CON ARCO")
    woolplaced: int = Field(alias="LANAS COLOCADAS")

class ArenaPVP(BaseModel):
    """Model for ArenaPVP.

    Args:
        victories (int): How many wins the player has.
        murders (int): How many murders the player has.
        lost (int): How many games the player has lost.
    """

    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    lost: int = Field(alias="PERDIDAS")

class HungerGames(BaseModel):
    """ Model for Hunger Games.

    Args: 
        victories (int): Number of victories the player has.
        murders (int): Number of murders the player has.
        deaths (int): Number of death the player has.
    """
    victories: int = Field(alias="VICTORIAS")
    murders: int = Field(alias="ASESINATOS")
    deaths: int = Field(alias="MUERTES")


class Universocraft(BaseModel):
    """Universocraft model.

    Args:
        DestoryNexus (DestoryNexus): DestoryNexus stats.
        SkyWars (SkyWars): SkyWars stats.
        LuckyWars (SkyWars): LuckyWars stats.
        EggWars (EggWars): EggWars stats.
        BedWars (BedWars): BedWars stats.
        TeamSkyWars (SkyWars): TeamSkyWars stats.
        SpeedBuilders (SpeedBuilders): SpeedBuilders stats.
        BuildBattle (BuildBattle): BuildBattle stats.
        EscapeBeast (EscapeBeast): Escape the Beast stats.
        PartyGames (PartyGames): PartyGames stats.
        HungerGames (HungerGames): HungerGames stats.
        SkyPit (SkyPit): SkyPit stats.
        ArenaPVP (ArenaPVP): ArenaPVP stats.
        UHC (UHC): UHC stats.
        MurderMystery (MurderMystery): MurderMystery stats.
        CaptureWool (CaptureWool): Capture the Woll stats.
    """

    DestoryNexus: DestoryNexus
    SkyWars: SkyWars
    LuckyWars: SkyWars
    EggWars: EggWars
    BedWars: BedWars
    TeamSkyWars: SkyWars
    SpeedBuilders: SpeedBuilders
    BuildBattle: BuildBattle
    EscapeBeast: EscapeBeast
    PartyGames: PartyGames
    HungerGames: HungerGames
    SkyPit: SkyPit
    ArenaPVP: ArenaPVP
    UHC: UHC
    MurderMystery: MurderMystery
    CaptureWool: CaptureWool

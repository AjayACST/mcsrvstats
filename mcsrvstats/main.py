"""Main functions for mcsrvstats."""
import json
from typing import Any
from typing import Dict
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup

from .exceptions import ApiError
from .exceptions import PlayerNotFoundError
from .models import Aether
from .models import ArenaPVP
from .models import Atlas
from .models import Aztec
from .models import BedWars
from .models import BedWarsGomme
from .models import BuildBattle
from .models import CaptureWool
from .models import Classes
from .models import Cookies
from .models import Cores
from .models import Creative
from .models import DestoryNexus
from .models import EggWars
from .models import EnderGames
from .models import EscapeBeast
from .models import Factions
from .models import GommeHD
from .models import GunGame
from .models import Hardcore
from .models import HCF
from .models import HungerGames
from .models import Islands
from .models import Kitpvp
from .models import LuckyWars
from .models import Manacube
from .models import MasterBuilders
from .models import MurderMystery
from .models import Oasis
from .models import Parkour
from .models import PartyGames
from .models import Practice
from .models import QuickSurvivalGames
from .models import SkyPit
from .models import SkyWars
from .models import SkyWarsGomme
from .models import Soup
from .models import SpeedBuilders
from .models import SpeedUHC
from .models import Survival
from .models import SurvivalGames
from .models import TeamSkyWars
from .models import TTT
from .models import UHC
from .models import Universocraft
from .models import Veltpvp
from .models import WyncraftClasses


class Client:
    """Client class."""

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        """Initialises class and creates aiohttp session."""
        if session:
            self.session = session
            return
        self.session = aiohttp.ClientSession()

    async def close(self) -> None:
        """Used for safe client cleanup and stuff."""
        await self.session.close()

    async def _get_html(self, url: str) -> str:
        """Get html from api.

        Args:
            url (str): url of api

        Raises:
            ApiError: error if invalid response

        Returns:
            str: raw html
        """
        async with self.session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                return html
            raise ApiError("Api response not succesful")

    async def _get_json(self, url: str) -> Dict[str, Any]:
        """Get json response from api.

        Args:
            url (str): url of api

        Raises:
            ApiError: error if invalid response

        Returns:
            Dict[str, Any]: json response
        """
        async with self.session.get(url) as resp:
            if resp.status == 200:
                data: Dict[str, Any] = await resp.json()
                return data
            raise ApiError("Api response not succesful")

    async def manacube(self, username: str) -> Manacube:
        """Manacube player stats.

        Args:
            username (str): username of player.

        Raises:
            PlayerNotFoundError: error if player not found.

        Returns:
            Manacube: object containing players manacube data.
        """
        url = f"https://manacube.com/stats_data/fetch.php?username={username}"
        html_data = await self._get_html(url)
        json_data = json.loads(html_data)

        if not json_data["exists"]:
            raise PlayerNotFoundError(username=username)

        parkour_manacube = Parkour.parse_obj(json_data["parkour"])
        aztec_manacube = Aztec.parse_obj(json_data["aztec"])
        oasis_manacube = Oasis.parse_obj(json_data["oasis"])
        islands_manacube = Islands.parse_obj(json_data["islands"])
        survival_manacube = Survival.parse_obj(json_data["survival"])
        factions_manacube = Factions.parse_obj(json_data["factions"])
        aether_manacube = Aether.parse_obj(json_data["aether"])
        atlas_manacube = Atlas.parse_obj(json_data["atlas"])
        creative_manacube = Creative.parse_obj(json_data["creative"])
        kitpvp_manacube = Kitpvp.parse_obj(json_data["kitpvp"])

        return Manacube(
            exists=json_data["exists"],
            level=json_data["level"],
            rank=json_data["rank"],
            cubits=json_data["cubits"],
            firstseen=json_data["firstSeen"],
            lastseen=json_data["lastSeen"],
            lastseenago=json_data["lastSeenAgo"],
            parkour=parkour_manacube,
            aztec=aztec_manacube,
            oasis=oasis_manacube,
            islands=islands_manacube,
            survival=survival_manacube,
            factions=factions_manacube,
            aether=aether_manacube,
            atlas=atlas_manacube,
            creative=creative_manacube,
            kitpvp=kitpvp_manacube,
        )

    async def wynncraft_classes(self, username: str) -> WyncraftClasses:
        """Wynncraft player classes.

        Args:
            username (str): username of player

        Raises:
            PlayerNotFoundError: error if player not found.

        Returns:
            WyncraftClasses: object containing the players classes
        """
        url = f"https://api.wynncraft.com/v2/player/{username}/stats"
        json_data = await self._get_json(url)
        data = []

        if json_data["code"] == 400:
            raise PlayerNotFoundError(username=username)

        for _class in json_data["data"][0]["classes"]:
            data.append(Classes.parse_obj(_class))
        return WyncraftClasses(classes=data)

    # async def blocksmc(self, username: str) -> Dict[str, Any]:
    #     """Blocksmc player stats.

    #     Args:
    #         username (str): username of player

    #     Returns:
    #         Dict[str, Any]: Dict[str, Any]ionary of player stats
    #     """
    #     url = f"https://blocksmc.com/player/{username}"
    #     html = await self._get_html(url)
    #     soup = BeautifulSoup(html, "lxml")
    #     rank = (
    #         soup.find("p", {"class": ["profile-rank"]})
    #         .get_text()
    #         .replace("\n", "")
    #         .strip()
    #     )

    #     timeplayed = (
    #         soup.find("h1", {"dir": ["ltr"]}).get_text().replace("\n", "").strip()
    #     )
    #     data = {"rank": rank, "timeplayed": timeplayed, "game_stats": []}

    #     for game in soup.find_all("div", {"class": "col-xl-4"}):
    #         stats = {}
    #         game_name = (
    #             game.find("div", {"class": "title"})
    #             .get_text()
    #             .replace("\n", "")
    #             .strip()
    #         )
    #         for stat in game.find_all("li"):
    #             stat_name = (
    #                 stat.find("div", {"class": "key"})
    #                 .get_text()
    #                 .replace("\n", "")
    #                 .strip()
    #             )
    #             stat_val = int(stat.find("div", {"class": "val"}).get_text())
    #             stats[stat_name] = stat_val
    #         data["game_stats"].append({game_name: stats})
    #     return data

    async def universocraft(self, username: str) -> Universocraft:
        """Universocraft player stats.

        Args:
            username (str): username of player

        Raises:
            PlayerNotFoundError: error if player not found.
            ApiError: If one of the games is under maintenance.

        Returns:
            Universocraft: object containing the players stats.
        """
        url = f"https://stats.universocraft.com/stats.php?player={username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        data = []

        if soup.find("div", {"class": "main-content-error"}):
            raise PlayerNotFoundError(username=username)
        for game in soup.find_all("div", {"class": "game"}):
            stats = {}
            game_name = game.find("h2").get_text().replace("\n", "").strip()
            if "mantenimiento" in game.find("p").get_text().replace("\n", "").strip():
                raise ApiError("Api response not succesful")
            for stat in game.find_all("div", {"class": "game-stat"}):
                stat_val = stat.find("p", {"class": "game-stat-count"}).get_text()
                stat_name = stat.find("p", {"class": "game-stat-title"}).get_text()
                stats[stat_name] = stat_val
            data.append({game_name: stats})

        return Universocraft(
            DestoryNexus=DestoryNexus.parse_obj(data[0]["Destruye el Nexus"]),
            SkyWars=SkyWars.parse_obj(data[1]["SkyWars"]),
            LuckyWars=LuckyWars.parse_obj(data[2]["LuckyWars"]),
            EggWars=EggWars.parse_obj(data[3]["EggWars"]),
            BedWars=BedWars.parse_obj(data[4]["BedWars"]),
            TeamSkyWars=TeamSkyWars.parse_obj(data[5]["TeamSkyWars"]),
            SpeedBuilders=SpeedBuilders.parse_obj(data[6]["SpeedBuilders"]),
            BuildBattle=BuildBattle.parse_obj(data[7]["BuildBattle"]),
            EscapeBeast=EscapeBeast.parse_obj(data[8]["Escapa de la Bestia"]),
            PartyGames=PartyGames.parse_obj(data[9]["Party Games"]),
            HungerGames=HungerGames.parse_obj(data[10]["Juegos del Hambre"]),
            SkyPit=SkyPit.parse_obj(data[11]["SkyPit"]),
            ArenaPVP=ArenaPVP.parse_obj(data[12]["ArenaPvP"]),
            UHC=UHC.parse_obj(data[13]["UHC"]),
            MurderMystery=MurderMystery.parse_obj(data[14]["MurderMystery"]),
            CaptureWool=CaptureWool.parse_obj(data[15]["Captura la Lana"]),
        )

    async def gommehd(self, username: str) -> GommeHD:
        """Gommehd player stats.

        Args:
            username (str): username of player

        Raises:
            PlayerNotFoundError: error if player not found.

        Returns:
            GommeHD: object containing player stats.
        """
        url = f"https://www.gommehd.net/player/index?playerName={username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        data = []

        if not soup.find("span", {"class": "username"}):
            raise PlayerNotFoundError(username=username)

        for game in soup.find_all("div", {"class": "stat-table"}):
            stats = {}
            game_name = game.find("h5").get_text().replace("\n", "").strip()
            for stat in game.find_all("li"):
                stat_val = stat.find("span", {"class": "score"}).get_text()
                stat_name = (
                    stat.get_text().replace("\n", "").strip().replace(stat_val, "")
                )
                stats[stat_name] = stat_val
            data.append({game_name: stats})

        return GommeHD(
            TTT=TTT.parse_obj(data[0]["TTT"]),
            BedWars=BedWarsGomme.parse_obj(data[1]["BedWars"]),
            SkyWars=SkyWarsGomme.parse_obj(data[2]["SkyWars"]),
            SurvivalGames=SurvivalGames.parse_obj(data[3]["SurvivalGames"]),
            EnderGames=EnderGames.parse_obj(data[4]["EnderGames"]),
            QuickSurvivalGames=QuickSurvivalGames.parse_obj(
                data[5]["QuickSurvivalGames"]
            ),
            Cores=Cores.parse_obj(data[6]["Cores"]),
            GunGame=GunGame.parse_obj(data[7]["GunGame"]),
            SpeedUHC=SpeedUHC.parse_obj(data[8]["SpeedUHC"]),
            MasterBuilders=MasterBuilders.parse_obj(data[9]["MasterBuilders"]),
            Cookies=Cookies.parse_obj(data[10]["Cookies"]),
            Hardcore=Hardcore.parse_obj(data[11]["Hardcore"]),
        )

    async def veltpvp(self, username: str) -> Veltpvp:
        """Veltpvp player stats.

        Args:
            username (str): username of player

        Returns:
            Veltpvp: object containing player stats.
        """
        url = f"https://www.veltpvp.com/u/{username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        rank = soup.find("div", {"id": "profile"}).find("h2").get_text().strip()

        if not soup.find("div", {"class": "bottom"}):
            last_seen = "N/A"
        else:
            last_seen = (
                soup.find("div", {"class": "bottom"})
                .get_text()
                .split("\n")[2]
                .replace("\xa0", " ")
                .strip()
            )

        if not soup.find("div", {"class": "top"}):
            current_status = "N/A"
        else:
            current_status = soup.find("div", {"class": "top"}).get_text().strip()

        info = soup.find_all("div", {"class": "element"})[1].get_text().split("\n")
        first_joined = info[3].strip()
        time_played = info[5].replace("\xa0", " ").strip()
        monthly_views = info[7].strip()

        # first stat is special
        first_game = soup.find("a", {"class": "server"})
        game_name = (
            first_game.find("div", {"class": "server-header"}).get_text().strip()
        )
        stats = {}
        for stat in first_game.find_all("div", {"class": "server-stat"}):
            stat_name = (
                stat.find("div", {"class": "server-stat-description"})
                .get_text()
                .strip()
            )
            stat_val = (
                stat.find("div", {"class": "server-stat-number"})
                .get_text()
                .strip()
                .replace("\xa0", " ")
            )
            stats[stat_name] = stat_val
        hcf = HCF.parse_obj(stats)

        for game in soup.find_all(
            "div", {"class": "server"}
        ):  # pragma: no cover (due to bug in coverage.py)
            if game.find("span"):
                break
            game_name = game.find("div", {"class": "server-header"}).get_text().strip()
            stats = {}
            for stat in game.find_all("div", {"class": "server-stat"}):
                stat_name = (
                    stat.find("div", {"class": "server-stat-description"})
                    .get_text()
                    .strip()
                )
                stat_val = (
                    stat.find("div", {"class": "server-stat-number"}).get_text().strip()
                )
                stats[stat_name] = stat_val
            if game_name == "Practice":
                practice = Practice.parse_obj(stats)
            elif game_name == "Soup":
                soup = Soup.parse_obj(stats)

        return Veltpvp(
            Rank=rank,
            LastSeen=last_seen,
            CurrentStatus=current_status,
            FirstJoined=first_joined,
            TimePlayed=time_played,
            MonthlyViews=monthly_views,
            HCF=hcf,
            Practice=practice,
            Soup=soup,
        )

"""Main functions for mcsrvstats."""
import json
from typing import Any
from typing import Dict
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup

from .exceptions.exceptions import ApiError, PlayerNotFound
from .models import *

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

        Returns:
            Manacube: object containing players manacube data.
        """
        url = f"https://manacube.com/stats_data/fetch.php?username={username}"
        html_data = await self._get_html(url)
        json_data = json.loads(html_data)

        if not json_data["exists"]:
            raise PlayerNotFound(username=username)

        parkour_manacube=Parkour.parse_obj(json_data["parkour"])
        aztec_manacube=Aztec.parse_obj(json_data["aztec"])
        oasis_manacube=Oasis.parse_obj(json_data["oasis"])
        islands_manacube=Islands.parse_obj(json_data["islands"])
        survival_manacube=Survival.parse_obj(json_data["survival"])
        factions_manacube=Factions.parse_obj(json_data["factions"])
        aether_manacube=Aether.parse_obj(json_data["aether"])
        atlas_manacube= Atlas.parse_obj(json_data["atlas"])
        creative_manacube=Creative.parse_obj(json_data["creative"])
        kitpvp_manacube= Kitpvp.parse_obj(json_data["kitpvp"])

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

        Returns:
            WyncraftClasses: object containing the players classes
        """
        url = f"https://api.wynncraft.com/v2/player/{username}/stats"
        json_data = await self._get_json(url)
        data = []

        if json_data["code"] == 400:
            raise PlayerNotFound(username=username)

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

        Returns:
            Universocraft: object containing the players stats.
        """
        url = f"https://stats.universocraft.com/stats.php?player={username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")

        if soup.find("div", {"class": "main-content-error"}):
            raise PlayerNotFound(username=username)
        for game in soup.find_all("div", {"class": "game"}):
            stats = {}
            game_name = game.find("h2").get_text().replace("\n", "").strip()
            for stat in game.find_all("div", {"class": "game-stat"}):
                stat_val = stat.find("p", {"class": "game-stat-count"}).get_text()
                stat_name = stat.find("p", {"class": "game-stat-title"}).get_text()
                stats[stat_name] = stat_val
            if game_name == "Destruye el Nexus":
                destory_nexus=DestoryNexus.parse_obj(stats)
            elif game_name == "SkyWars":
                sky_wars=SkyWars.parse_obj(stats)
            elif game_name == "LuckyWars":
                lucky_wars=SkyWars.parse_obj(stats)
            elif game_name == "EggWars":
                egg_wars=EggWars.parse_obj(stats)
            elif game_name == "BedWars":
                bed_wars=BedWars.parse_obj(stats)
            elif game_name == "TeamSkyWars":
                team_sky_wars=SkyWars.parse_obj(stats)
            elif game_name == "SpeedBuilders":
                speed_builders=SpeedBuilders.parse_obj(stats)
            elif game_name == "BuildBattle":
                build_battle=BuildBattle.parse_obj(stats)
            elif game_name == "Escapa de la Bestia":
                escape_beast=EscapeBeast.parse_obj(stats)
            elif game_name == "Party Games":
                party_games=PartyGames.parse_obj(stats)
            elif game_name == "Juegos del Hambre":
                hunger_games=HungerGames.parse_obj(stats)
            elif game_name == "SkyPit":
                sky_pit=SkyPit.parse_obj(stats)
            elif game_name == "ArenaPvP":
                arena_pvp=ArenaPVP.parse_obj(stats)
            elif game_name == "UHC":
                uhc=UHC.parse_obj(stats)
            elif game_name == "MurderMystery":
                murder_mystery=MurderMystery.parse_obj(stats)
            elif game_name == "Captura la Lana":
                capture_wool=CaptureWool.parse_obj(stats)

        return Universocraft(
            DestoryNexus=destory_nexus,
            SkyWars=sky_wars,
            LuckyWars=lucky_wars,
            EggWars=egg_wars,
            BedWars=bed_wars,
            TeamSkyWars=team_sky_wars,
            SpeedBuilders=speed_builders,
            BuildBattle=build_battle,
            EscapeBeast=escape_beast,
            PartyGames=party_games,
            HungerGames=hunger_games,
            SkyPit=sky_pit,
            ArenaPVP=arena_pvp,
            UHC=uhc,
            MurderMystery=murder_mystery,
            CaptureWool=capture_wool
        )

    async def minesaga(self, username: str) -> Dict[str, Any]:
        """Minesaga player stats.

        Args:
            username (str): username of player

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of player stats
        """
        url = f"https://www.minesaga.org/player/{username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        main_info = soup.find("div", {"class": ["dd-profile-details"]})
        joined = main_info.find("h4").get_text().strip()
        data = {
            "joined": joined,
            "last_seen": main_info.findAll("span")[1].get_text().strip(),
            "play_time": main_info.findAll("span")[2].get_text().strip(),
            "game_stats": [],
        }

        for game in soup.find_all("div", {"class": "dd-section col-md-4"}):
            stats = {}
            game_name = (
                game.find("div", {"class": "dd-box-title"})
                .get_text()
                .replace("\n", "")
                .strip()
            )
            for stat in game.find_all("dl"):
                stat_name = stat.find("dt").get_text().replace("\n", "").strip()
                stat_val = stat.find("dd").get_text()
                stats[stat_name] = stat_val
            data["game_stats"].append({game_name: stats})

        return data

    async def gommehd(self, username: str) -> Dict[str, Any]:
        """Gommehd player stats.

        Args:
            username (str): username of player

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of player stats
        """
        url = f"https://www.gommehd.net/player/index?playerName={username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        data: Dict[str, Any] = {"game_stats": []}
        for game in soup.find_all("div", {"class": "stat-table"}):
            stats = {}
            game_name = game.find("h5").get_text().replace("\n", "").strip()
            for stat in game.find_all("li"):
                stat_val = stat.find("span", {"class": "score"}).get_text()
                stat_name = (
                    stat.get_text().replace("\n", "").strip().replace(stat_val, "")
                )
                stats[stat_name] = stat_val
            data["game_stats"].append({game_name: stats})
        return data

    async def veltpvp(self, username: str) -> Dict[str, Any]:
        """Veltpvp player stats.

        Args:
            username (str): username of player

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of player stats
        """
        url = f"https://www.veltpvp.com/u/{username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        rank = soup.find("div", {"id": "profile"}).find("h2").get_text().strip()
        last_seen = (
            soup.find("div", {"class": "bottom"})
            .get_text()
            .split("\n")[2]
            .replace("\xa0", " ")
            .strip()
        )
        current_status = soup.find("div", {"class": "top"}).get_text().strip()
        info = soup.find_all("div", {"class": "element"})[1].get_text().split("\n")
        first_joined = info[3].strip()
        time_played = info[5].replace("\xa0", " ").strip()
        monthly_views = info[7].strip()
        data = {
            "rank": rank,
            "last_seen": last_seen,
            "current_status": current_status,
            "first_joined": first_joined,
            "time_played": time_played,
            "monthly_views": monthly_views,
            "game_stats": [],
        }

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
                stat.find("div", {"class": "server-stat-number"}).get_text().strip()
            )
            stats[stat_name] = stat_val
        data["game_stats"].append({game_name: stats})

        for game in soup.find_all("div", {"class": "server"}):
            if not game.find("div", {"class": "server unknown"}):
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
            data["game_stats"].append({game_name: stats})
        return data

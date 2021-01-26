"""Main functions for mcsrvstats."""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup

from .exceptions.exceptions import ApiError
from .models import Aether
from .models import Atlas
from .models import Aztec
from .models import Creative
from .models import Factions
from .models import HiveAchievements
from .models import HiveRank
from .models import HiveStatus
from .models import Islands
from .models import Kitpvp
from .models import Manacube
from .models import Oasis
from .models import Parkour
from .models import Survival

# from .models import Classes

# from .models import WyncraftClasses


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

    async def hive_mc_achievments(self, username: str) -> HiveAchievements:
        """Hive Minceaft player achievements.

        Args:
            username (str): username of player

        Returns:
            HiveAchievements: object containing all achievements for a player.
        """
        url = f"http://api.hivemc.com/v1/player/{username}"
        json_data = await self._get_json(url)
        data: List[str] = []
        for ach in json_data["achievements"]:
            data.append(ach)
        return HiveAchievements(all_achievements=data)

    async def hive_mc_status(self, username: str) -> HiveStatus:
        """Hive Minecraft player status.

        Args:
            username (str): username of player

        Returns:
            HiveStatus: Object containing the players current status.
        """
        url = f"http://api.hivemc.com/v1/player/{username}"
        json_data = await self._get_json(url)
        return HiveStatus(
            description=json_data["status"]["description"],
            game=json_data["status"]["game"],
        )

    async def hive_mc_game_stats(self, username: str, game: str) -> Dict[str, Any]:
        """Hive Minecraft game stats of a player.

        Args:
            username (str): username of player
            game (str): game for stats

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of stats.
        """
        url = f"http://api.hivemc.com/v1/player/{username}/{game}"
        json_data = await self._get_json(url)
        data = {"stats": [json_data]}
        return data

    async def hive_mc_rank(self, username: str) -> HiveRank:
        """Hive Minecraft rank.

        Args:
            username (str): username of player

        Returns:
            HiveRank: object containing the players rank on Hive.
        """
        url = f"http://api.hivemc.com/v1/player/{username}"
        json_data = await self._get_json(url)
        return HiveRank(rank=json_data["rankName"])

    async def manacube(self, username: str) -> Manacube:
        """Manacube player stats.

        Args:
            username (str): username of player

        Returns:
            Manacube: object containing players manacube data.
        """
        url = f"https://manacube.com/stats_data/fetch.php?username={username}"
        html_data = await self._get_html(url)
        json_data = json.loads(html_data)

        parkour_manacube = Parkour(
            playtime=json_data["parkour"]["playtime"],
            mana=json_data["parkour"]["mana"],
            score=json_data["parkour"]["score"],
            courses=json_data["parkour"]["courses"],
        )

        aztec_manacube = Aztec(
            playtime=json_data["aztec"]["playtime"],
            mobkills=json_data["aztec"]["mobKills"],
            mana=json_data["aztec"]["mana"],
            money=json_data["aztec"]["money"],
        )

        oasis_manacube = Oasis(
            playtime=json_data["oasis"]["playtime"],
            mobkills=json_data["oasis"]["mobKills"],
            mana=json_data["oasis"]["mana"],
            money=json_data["oasis"]["money"],
        )

        islands_manacube = Islands(
            playtime=json_data["islands"]["playtime"],
            mobkills=json_data["islands"]["mobKills"],
            silver=json_data["islands"]["silver"],
            money=json_data["islands"]["money"],
        )

        survival_manacube = Survival(
            playtime=json_data["survival"]["playtime"],
            mobkills=json_data["survival"]["mobKills"],
            money=json_data["survival"]["money"],
            quests=json_data["survival"]["quests"],
        )

        factions_manacube = Factions(
            playtime=json_data["factions"]["playtime"],
            kills=json_data["factions"]["kills"],
            mobkills=json_data["factions"]["mobkills"],
            money=json_data["factions"]["money"],
        )

        aether_manacube = Aether(
            playtime=json_data["aether"]["playtime"],
            mininglevel=json_data["aether"]["miningLevel"],
            money=json_data["aether"]["money"],
            rebirths=json_data["aether"]["rebirths"],
        )

        atlas_manacube = Atlas(
            playtime=json_data["atlas"]["playtime"],
            mininglevel=json_data["atlas"]["miningLevel"],
            money=json_data["atlas"]["money"],
            rebirths=json_data["atlas"]["rebirths"],
        )

        creative_manacube = Creative(
            playtime=json_data["creative"]["playtime"],
            blocksplaced=json_data["creative"]["blocksplaced"],
            blocksbroken=json_data["creative"]["blocksbroken"],
        )

        kitpvp_manacube = Kitpvp(
            playtime=json_data["kitpvp"]["playtime"],
            level=json_data["kitpvp"]["level"],
            money=json_data["kitpvp"]["money"],
            kills=json_data["kitpvp"]["kills"],
        )

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

    # async def wynncraft_classes(self, username: str) -> WyncraftClasses:
    #     """Wynncraft player classes.

    #     Args:
    #         username (str): username of player

    #     Returns:
    #         WyncraftClasses: object containing the players classes
    #     """
    #     url = f"https://api.wynncraft.com/v2/player/{username}/stats"
    #     json_data = await self._get_json(url)
    #     data = []
    #     for _class in json_data["data"][0]["classes"]:
    #         data.append(
    #             Classes(
    #                 class_name=_class["name"],
    #                 class_level=_class["level"],
    #                 class_deaths=_class["deaths"]
    #             )
    #         )
    #     return WyncraftClasses(
    #         classes=data
    #     )

    async def blocksmc(self, username: str) -> Dict[str, Any]:
        """Blocksmc player stats.

        Args:
            username (str): username of player

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of player stats
        """
        url = f"https://blocksmc.com/player/{username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        rank = (
            soup.find("p", {"class": ["profile-rank"]})
            .get_text()
            .replace("\n", "")
            .strip()
        )

        timeplayed = (
            soup.find("h1", {"dir": ["ltr"]}).get_text().replace("\n", "").strip()
        )
        data = {"rank": rank, "timeplayed": timeplayed, "game_stats": []}

        for game in soup.find_all("div", {"class": "col-xl-4"}):
            stats = {}
            game_name = (
                game.find("div", {"class": "title"})
                .get_text()
                .replace("\n", "")
                .strip()
            )
            for stat in game.find_all("li"):
                stat_name = (
                    stat.find("div", {"class": "key"})
                    .get_text()
                    .replace("\n", "")
                    .strip()
                )
                stat_val = int(stat.find("div", {"class": "val"}).get_text())
                stats[stat_name] = stat_val
            data["game_stats"].append({game_name: stats})
        return data

    async def universocraft(self, username: str) -> Dict[str, Any]:
        """Universocraft player stats.

        Args:
            username (str): username of player

        Returns:
            Dict[str, Any]: Dict[str, Any]ionary of player stats
        """
        url = f"https://stats.universocraft.com/stats.php?player={username}"
        html = await self._get_html(url)
        soup = BeautifulSoup(html, "lxml")
        data: Dict[str, Any] = {"game_stats": []}
        for game in soup.find_all("div", {"class": "game"}):
            stats = {}
            game_name = game.find("h2").get_text().replace("\n", "").strip()
            for stat in game.find_all("div", {"class": "game-stat"}):
                stat_val = stat.find("p", {"class": "game-stat-count"}).get_text()
                stat_name = stat.find("p", {"class": "game-stat-title"}).get_text()
                stats[stat_name] = stat_val
            data["game_stats"].append({game_name: stats})
        return data

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

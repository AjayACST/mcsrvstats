import aiohttp
from bs4 import BeautifulSoup

async def get_html(url, session):
    async with session.get(url) as resp:
        if resp.status == 200:
            html = await resp.text()
            return html
        else:
            return False

async def blocksmc(username, session):
    url = f"https://blocksmc.com/player/{username}"
    html = get_html(url, session)
    soup = BeautifulSoup(html.content, "lxml")
    name = soup.find("h1", {"class": [".profile-header"]}).get_text().strip()
    rank = soup.find({"class": [".profile-rank"]}).get_text().replace("\n", "").strip()
    timePlayed = soup.find("h1", {"dir": ["ltr"]}).get_text().replace("\n", "").strip()
    data = [name, rank, timePlayed]
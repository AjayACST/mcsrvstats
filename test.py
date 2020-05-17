import requests
import asyncio
import json



async def get_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        json_src = r.json()
        return json_src
    else:
        return False

async def hypixelHungerGames(username,key):
    url = f"https://api.hypixel.net/player?key={key}&name={username}"
    json_data = await get_json(url)
    str_json = json.dumps(json_data)
    json_new = json.loads(str_json)
    data = {"game_stats": []}
    if json_new['player'] is None:
        return False
    else:
        for game in json_new['player']['stats']:
            hypixelGames = json_new['player']['stats'][game] if game in json_new['player']['stats'] else 0
            data["game_stats"].append({game: [hypixelGames]})
    print(data)


async def run_def(username):
    await hypixelHungerGames(username, "218c4847-450e-4218-aa99-bcc08c7a6595")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_def("Arrow_Plays"))
    loop.close()
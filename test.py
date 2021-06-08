import mcsrvstats
import asyncio

async def main():
    client = mcsrvstats.Client()
    test = await client.universocraft("uBored")
    print(test)
    await client.close()

asyncio.run(main())
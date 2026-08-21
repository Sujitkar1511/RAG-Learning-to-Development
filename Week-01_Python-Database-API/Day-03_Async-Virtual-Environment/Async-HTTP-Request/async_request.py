import asyncio
import aiohttp


async def fetch(session, url):

    async with session.get(url) as response:

        return await response.text()


async def main():

    url = "https://jsonplaceholder.typicode.com/todos"

    async with aiohttp.ClientSession() as session:

        result = await fetch(session, url)

        print(result)


asyncio.run(main())
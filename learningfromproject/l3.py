import asyncio


async def worker():
    print("hello world this time we have to gone to other places ")
    await asyncio.sleep(3)
    print("brooowww")

loop = asyncio.get_event_loop()
loop.run_until_complete(worker())
loop.close()

print("main page continues")

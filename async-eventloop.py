import asyncio
import datetime

async def like():
    # code for task 1
    await asyncio.sleep(1)
    print("Task 1 like done")

async def share():
    # code for task 2
    await asyncio.sleep(2)
    print("Task 2 share done")

async def subscribe():
    # code for task 3
    await asyncio.sleep(0.5)
    print("Task 3 subscribe done")

async def run_tasks():
    start = datetime.datetime.now()
    # create event loop
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(like()),
        loop.create_task(like()),
        loop.create_task(like()),       
        loop.create_task(share()),
        loop.create_task(share()),
        loop.create_task(share()),        
        loop.create_task(subscribe()),
        loop.create_task(subscribe())    
        ]
    # wait for tasks to complete
    loop.run_until_complete(asyncio.gather(*tasks))

    dt = datetime.datetime.now() - start

    print("Synchronous version done in {:,0.2f} seconds".format(dt.total_seconds))

    loop.close()
#asyncio.run(run_tasks())
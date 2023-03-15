import asyncio

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
    # create tasks
    t1 = asyncio.create_task(like())
    t2 = asyncio.create_task(share())
    t3 = asyncio.create_task(subscribe())

    # wait for tasks to complete
    await asyncio.gather(t1, t2, t3)

asyncio.run(run_tasks())
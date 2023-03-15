import asyncio
import time

import colorama
from colorama import Fore, Style

colorama.init()

async def task1():
    print(Fore.CYAN + "Task 1 started"+ Style.RESET_ALL)
    await asyncio.sleep(2)
    print(Fore.CYAN + "Task 1 finished" + Style.RESET_ALL)

async def task2():
    print(Fore.GREEN + "Task 2 started" + Style.RESET_ALL)
    await asyncio.sleep(1)
    print(Fore.GREEN + "Task 2 finished" + Style.RESET_ALL)

async def task3():
    print(Fore.YELLOW + "Task 3 started" + Style.RESET_ALL)
    await asyncio.sleep(3)
    print(Fore.YELLOW + "Task 3 finished" + Style.RESET_ALL)

loop = asyncio.get_event_loop()
try:
    tasks = [task1(), task1(), task2(), task2(), task2(), task3(), task3()]
    start_time = time.time()
    loop.run_until_complete(asyncio.gather(*tasks))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total elapsed time: {elapsed_time:.2f} seconds")
finally:
    loop.close()
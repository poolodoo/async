import asyncio

async def compute_square(x):
    print(f"Computing square of {x}")
    await asyncio.sleep(1.0)
    return x ** 2

async def print_squares(numbers):
    tasks = []
    for n in numbers:
        task = asyncio.create_task(compute_square(n))
        tasks.append(task)
    for task in tasks:
        result = await task
        print(f"Square of {result} is {result**2}")

async def main():
    await print_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    asyncio.run(main())
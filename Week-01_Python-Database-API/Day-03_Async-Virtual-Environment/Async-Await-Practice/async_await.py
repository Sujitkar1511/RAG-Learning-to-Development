import asyncio

async def Task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def Task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def Task3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 completed")

async def main():
    await asyncio.gather(Task1(), Task2(), Task3())

# Run the main function
asyncio.run(main())
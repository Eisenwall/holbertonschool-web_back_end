#!/usr/bin/env python3
"""Module 1-concurrent_coroutines
Contains an asynchronous coroutine wait_n that spawns wait_random n times
and returns a list of all delays in ascending order.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with the specified max_delay.
    Return the list of delays in ascending order (without using sort).
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for future in asyncio.as_completed(tasks):
        result = await future
        delays.append(result)

    return delays

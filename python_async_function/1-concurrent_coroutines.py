#!/usr/bin/env python3
"""Module 1-concurrent_coroutines
Contains an asynchronous coroutine wait_n that spawns wait_random n times
and returns a list of all delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    Return the list of delays in ascending order (without using sort).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays

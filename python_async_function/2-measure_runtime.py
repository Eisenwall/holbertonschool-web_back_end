#!/usr/bin/env python3
"""Module 4-tasks
Contains an asynchronous coroutine task_wait_n that spawns
task_wait_random n times and returns a list of delays in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay.
    Return the list of delays in ascending order (without using sort).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays

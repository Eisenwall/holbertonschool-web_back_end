#!/usr/bin/env python3
"""Async generator that yields 10 random numbers with a 1-second delay"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that asynchronously yields a random number between 0 and 10
    every second for 10 iterations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""Async generator that yields 10 random numbers with a 1-second delay"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yield 10 random numbers between 0 and 10, one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

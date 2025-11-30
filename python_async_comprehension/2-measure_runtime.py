#!/usr/bin/env python3
"""Measure runtime of async_comprehension executed concurrently"""

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and return total runtime."""
    start = time.perf_counter()
    # Запускаем 4 экземпляра async_comprehension параллельно
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    return end - start
